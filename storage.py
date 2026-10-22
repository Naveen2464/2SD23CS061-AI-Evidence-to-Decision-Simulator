"""Small SQLite persistence layer for the single-case local training simulator.

For multi-user deployment, add authentication and tenant/session scoping before use.
"""
from __future__ import annotations
import json
import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).parent / "case_history.sqlite3"

def connect():
    con = sqlite3.connect(DB_PATH, timeout=10)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with connect() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS attempts (
          id INTEGER PRIMARY KEY AUTOINCREMENT, case_id TEXT NOT NULL,
          created_at TEXT NOT NULL, payload TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS requests (
          id INTEGER PRIMARY KEY AUTOINCREMENT, case_id TEXT NOT NULL,
          evidence_id TEXT NOT NULL, created_at TEXT NOT NULL, payload TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS releases (
          case_id TEXT NOT NULL, evidence_id TEXT NOT NULL, payload TEXT NOT NULL,
          released_at TEXT NOT NULL, PRIMARY KEY(case_id, evidence_id)
        );
        CREATE TABLE IF NOT EXISTS qa_history (
          id INTEGER PRIMARY KEY AUTOINCREMENT, case_id TEXT NOT NULL,
          created_at TEXT NOT NULL, payload TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS evidence_uploads (
          id INTEGER PRIMARY KEY AUTOINCREMENT, case_id TEXT NOT NULL,
          evidence_id TEXT NOT NULL, created_at TEXT NOT NULL, payload TEXT NOT NULL,
          UNIQUE(case_id, evidence_id)
        );
        """)

def load_items(table: str, case_id: str) -> list[dict[str, Any]]:
    if table not in {"attempts", "requests", "qa_history", "evidence_uploads"}:
        raise ValueError("Unsupported table")
    actual_table = "evidence_uploads" if table == "evidence_uploads" else table
    with connect() as con:
        rows = con.execute(f"SELECT payload FROM {actual_table} WHERE case_id=? ORDER BY id", (case_id,)).fetchall()
    return [json.loads(row["payload"]) for row in rows]

def save_item(table: str, case_id: str, created_at: str, payload: dict[str, Any]):
    if table not in {"attempts", "requests", "qa_history", "evidence_uploads"}:
        raise ValueError("Unsupported table")
    with connect() as con:
        if table == "evidence_uploads":
            con.execute("INSERT OR IGNORE INTO evidence_uploads(case_id,evidence_id,created_at,payload) VALUES(?,?,?,?)",
                        (case_id, str(payload.get("id", "")), created_at, json.dumps(payload, ensure_ascii=False)))
        elif table == "requests":
            con.execute("INSERT INTO requests(case_id,evidence_id,created_at,payload) VALUES(?,?,?,?)",
                        (case_id, str(payload.get("id", "")), created_at, json.dumps(payload, ensure_ascii=False)))
        else:
            con.execute(f"INSERT INTO {table}(case_id,created_at,payload) VALUES(?,?,?)",
                        (case_id, created_at, json.dumps(payload, ensure_ascii=False)))

def save_release(case_id: str, evidence_id: str, released_at: str, payload: dict[str, Any]):
    with connect() as con:
        con.execute("INSERT OR REPLACE INTO releases(case_id,evidence_id,payload,released_at) VALUES(?,?,?,?)",
                    (case_id, evidence_id, json.dumps(payload, ensure_ascii=False), released_at))

def load_releases(case_id: str) -> dict[str, dict[str, Any]]:
    with connect() as con:
        rows = con.execute("SELECT evidence_id,payload FROM releases WHERE case_id=?", (case_id,)).fetchall()
    return {row["evidence_id"]: json.loads(row["payload"]) for row in rows}
