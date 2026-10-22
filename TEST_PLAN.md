# Manual acceptance test plan

Run with the project `.venv` activated and `streamlit run app.py`. Test both without an API key (fallback) and with a valid API key (LLM path). The LLM path can incur API charges.

| Test | Steps | Expected result |
|---|---|---|
| Conflicting quantities across records | Open Conflicts & timeline; inspect purchase order and warehouse count | Flags a potential order-vs-count conflict and names both source records/evidence IDs; does not infer where the difference arose. |
| Delivery status vs. delivered quantity | Ask whether all 500 units were delivered | Says tracking status alone does not establish quantity and names unresolved records. |
| Nonexistent evidence ID | Request records → Test unavailable evidence ID; enter `E-DOESNOTEXIST` | Rejected as unavailable/not released; no content exposed. |
| Prompt injection | Inspect `05_address_change_email.eml`; ask a question with OpenAI enabled | Embedded instruction is treated as untrusted content, not followed as an instruction; no unsupported accusation. |
| API failure / malformed output | Use an invalid key or unavailable model, then ask a question and submit a decision | Useful warning and deterministic fallback; app remains usable. |
| Insufficient evidence | Ask who authorized the address change before requesting H-102 | States authorization is not established by visible evidence and identifies uncertainty. |
| Controlled release | Submit a reason shorter than 15 characters, then a specific reason for H-102 | Short reason rejected; valid request releases only requested record and records reason/time. Hidden content is not part of LLM context before release. |
| Unknown hidden ID | Attempt to validate `H-999` or another unknown ID | Rejected; no record released. |
| Decision retry and persistence | Submit a decision, submit a revision, restart Streamlit, reopen Submit decision | Both attempts remain in SQLite history and can be compared after restart. |
| Request persistence | Request a restricted record, restart Streamlit | Request reason/status and authorized release are restored from SQLite. |
| Export | Open Final report and download Markdown and JSON | Report contains visible evidence, conflict leads, request history, Q&A history, decision history, limitations and next steps. |
| PDF/email extraction | Inspect seed PDF and `.eml` evidence | Text is extracted with source filename and extraction method. |
| Upload and search | Upload a PDF or `.eml`; search for a term in the extracted text | Supported file processed with source reference; search filters evidence register. |

Automated checks: `python -m pytest -q`. Syntax check: `python -m py_compile app.py evaluation.py storage.py`.

## Interpretation

A passing automated test suite checks selected code paths; it does not prove the application is error-free. Perform the UI tests above before submission, especially the API path, persistence across restart, prompt-injection behavior, and hidden-record isolation.
