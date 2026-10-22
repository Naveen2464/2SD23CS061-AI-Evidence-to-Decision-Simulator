# AI Evidence-to-Decision Simulator

A Streamlit application for the **provided internship assignment**. It investigates a synthetic shipment discrepancy involving 500 electronic components valued at ₹18,00,000. The scenario and assignment requirements have been preserved; the sample records are synthetic and do not accuse any real party.

## Windows setup using a virtual environment

Use the Python version installed on your machine (Python 3.10 is a good choice for this project). Open PowerShell in the extracted project folder:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell says that `py -3.10` is unavailable, use `py -0p` to list installed Python versions and replace `3.10` with an installed compatible version. In VS Code, choose `.venv\Scripts\python.exe` using **Python: Select Interpreter**. The `.venv` directory is intentionally not included in the ZIP; create it locally using the commands above.

To deactivate the environment later:

```powershell
deactivate
```

## Optional OpenAI API integration

The app runs without an API key. Without one, the Q&A uses a conservative deterministic fallback and decision grading uses a transparent heuristic rubric. For LLM-powered evidence Q&A and criterion-level evaluation, set the key in the same PowerShell terminal before launching:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_MODEL="gpt-4o-mini"
streamlit run app.py
```

Use an API key you are authorized to use; API usage may incur charges. Never commit the key or put it in source files. A missing key, API error, or invalid model response is handled with a fallback and visible notice.

## Features mapped to the assignment

- Case workspace and case summary.
- Extraction from PDF, `.eml`, `.txt`, `.md`, `.csv`, and `.json` records, including user-uploaded files.
- Stable evidence IDs, source filename, extraction method, and claim-status metadata.
- Searchable evidence register, heuristic date timeline, and rule-based conflict leads with source references.
- Evidence-grounded Q&A with structured JSON when the API is configured; citations are checked against currently released evidence IDs.
- Restricted synthetic records kept in `hidden_records.json`. Before release, only title/description are shown to the user and the hidden contents are not included in LLM prompts. A reason of at least 15 characters is required to request a record. Release and reason are recorded in local SQLite history.
- Decision form collecting conclusion, supporting evidence, counterevidence, confidence, reasoning, and next action.
- Criterion-level evaluation, Python validation of score schema/ranges/evidence references, and Python-calculated total out of 100. Evidence-presence caps stop the LLM from awarding high support/traceability scores when no relevant IDs are selected.
- Fallback rubric when LLM is unavailable. Fallback is heuristic and clearly labelled; do not represent it as expert human grading.
- Decision attempts, evidence-request history, released-record state, and Q&A history persisted in `case_history.sqlite3` across app restarts for this local single-case training app.
- Attempt comparison and report export to Markdown and JSON.
- Tests for scoring bounds, invalid IDs, hidden evidence reference rejection, evidence-presence score caps, conflict-rule presence, and SQLite persistence.

## Run tests

```powershell
python -m pytest -q
```

## Evaluation rubric (100 points)

| Criterion | Maximum |
|---|---:|
| Uses relevant released evidence | 25 |
| Addresses counterevidence and conflicts | 20 |
| Calibrates uncertainty fairly | 20 |
| Chooses a useful next investigative step | 20 |
| Valid evidence IDs and source traceability | 15 |
| **Total** | **100** |

## Evidence and security boundaries

- A delivery-completed status is evidence of a recorded delivery event; it is **not, by itself, proof that all 500 units arrived**.
- Supplier dispatch statements, carrier scans, warehouse count entries, and address-change emails are claims/records with different evidentiary scope. The app does not infer fraud, theft, or responsibility from the current record set.
- Prompt-injection text in a document is untrusted evidence, not an instruction. The LLM system prompt explicitly says to ignore instructions embedded in documents.
- Python owns evidence-ID validation, hidden-record release checks, score-range validation, and final score arithmetic. LLM output is never accepted as the final total.
- Conflict detection and date parsing are heuristic leads, not complete semantic analysis or proof. The user should verify every flagged conflict against source documents.
- SQLite history is for a local, single-case training app. It is not a production multi-user access-control boundary. A real deployment needs authentication, per-user/per-case authorization, durable audit controls, upload limits, malware scanning, backups, and tests for concurrent access.
- Automated tests do not replace manual UI acceptance tests. Verify API behavior with a valid API key and verify the fallback path without one before submitting.
