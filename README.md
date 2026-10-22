🚀 AI Evidence-to-Decision Simulator

Turn scattered case documents into a clear, evidence-grounded investigation.

AI Evidence-to-Decision Simulator is an interactive Streamlit application built around a fictional shipment discrepancy. Explore source documents, trace claims to evidence, investigate conflicting records, ask evidence-based questions, request restricted records, and prepare a structured decision with a final report.

Demo case: 500 electronic components ordered for ₹18,00,000; the warehouse reports counting 420 units. The application helps examine the discrepancy without jumping to conclusions or assigning blame without evidence.

✨ Features

📁 Document workspace — review case materials and inspect extracted text from supported documents.

🔎 Evidence register — search records and track evidence IDs and source information.

🧭 Timeline and conflict leads — surface dates, quantity differences, and claims that need verification.

💬 Evidence-based Q&A — ask questions about the case and review supporting citations when available.

🔐 Controlled record requests — request restricted synthetic records with a reason and keep a local history of releases.

📝 Structured decision workspace — record a conclusion, supporting evidence, counterevidence, confidence, reasoning, and next steps.

📊 Decision evaluation — receive rubric-based feedback, with a transparent heuristic fallback when AI services are not configured.

💾 Local history — preserve decision attempts, requests, released-record state, and Q&A history in SQLite.

📄 Exportable reports — export the investigation report as Markdown and case state as JSON.

🖥️ Technology

Python 3.14

Streamlit

SQLite

Pytest

Optional AI integration, depending on the provider configured in the application.

⚙️ Installation (Windows + Python 3.14)

1. Check Python

Open PowerShell and run:

py -3.14 --version

2. Open the project folder

Open PowerShell or the VS Code terminal in your project directory:

cd "C:\path\to\ai_evidence_simulator"

Replace the example path with your actual project folder path.

3. Create and activate a virtual environment

py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1

If PowerShell blocks activation, run this in the same terminal, then activate again:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1

4. Install dependencies

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

5. Run the app

streamlit run app.py

Open the local address printed in the terminal, usually http://localhost:8501.

6. Run tests (optional)

python -m pytest -v

🔑 AI configuration

The app can use a fallback mode when an AI API key is not configured. For AI-powered features, follow the provider and environment-variable settings used by your local app.py. Never commit API keys or .env files to GitHub. API use may incur charges.

📂 Project structure

ai_evidence_simulator/
├── app.py
├── evaluation.py
├── storage.py
├── hidden_records.json
├── sample_documents/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore

The app may create local files, such as a SQLite history database and Python cache folders, when it runs.

🎯 Example investigation

The sample case compares the purchase order, supplier dispatch statement, carrier tracking, warehouse count, packing slip, and an address-change request. A delivery scan does not by itself prove the quantity received. The application highlights evidence gaps and follow-up actions rather than making unsupported accusations.

🔒 Privacy and safety

All parties and records in the sample scenario are fictional.

Treat document contents as source material, not instructions to the application.

Keep API keys and secrets out of source control.

SQLite history is intended for local, single-case training use, not production multi-user security.

📌 Notes

Python 3.14 is the intended setup. If a dependency fails to install, check whether its version in requirements.txt supports Python 3.14.

Timeline and conflict detection are heuristic aids; verify findings against the original records.

Automated tests are useful, but manually check the interface before submitting.
