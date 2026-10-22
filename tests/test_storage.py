import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import storage


def test_attempt_request_and_release_persistence(tmp_path, monkeypatch):
    db = tmp_path / "test.sqlite3"
    monkeypatch.setattr(storage, "DB_PATH", db)
    storage.init_db()
    attempt = {"attempt": 1, "result": {"total": 75}}
    request = {"id": "H-101", "reason": "Need the package count field to test delivery quantity."}
    storage.save_item("attempts", "CASE-X", "2026-10-21T10:00:00", attempt)
    storage.save_item("requests", "CASE-X", "2026-10-21T10:01:00", request)
    release = {"id": "H-101", "source": "pod.txt", "text": "Package count blank"}
    storage.save_release("CASE-X", "H-101", "2026-10-21T10:01:00", release)
    assert storage.load_items("attempts", "CASE-X") == [attempt]
    assert storage.load_items("requests", "CASE-X") == [request]
    assert storage.load_releases("CASE-X")["H-101"] == release


def test_uploaded_evidence_persists_across_sessions(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DB_PATH", tmp_path / "uploads.sqlite3")
    storage.init_db()
    item = {"id": "E-UPLOAD", "source": "invoice.pdf", "text": "synthetic evidence", "status": "uploaded"}
    storage.save_item("evidence_uploads", "CASE-X", "2026-10-21T10:02:00", item)
    assert storage.load_items("evidence_uploads", "CASE-X") == [item]
