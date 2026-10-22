Pasted code(6).py
Python
i want submit these assignment now and these app.py 
and reduce number of lines or code 
Pasted text(20261022-135136).txt
Document
which are unnessary file are there i want delete and  check if error exist after delteing 
delte any folder or it required
check these untill after words submit decision and final report next
Pasted markdown(9).md
File
Pasted text (2)(1).txt
Document
check these correct or not 
Pasted markdown(10).md
File

YES! ✅ You can submit your GitHub repository link instead of uploading the entire project folder to Google Drive, provided your evaluator accepts GitHub links.

Your project already has a GitHub repository:
MediXR GitHub Repository

Note: That is your MediXR repository, not your AI Evidence-to-Decision Simulator repository. You should upload the correct project to a separate repository.

What I recommend
Option 1 — Submit your GitHub link

Best if the instructions allow a GitHub repository URL.

Open GitHub.
Create a new repository named AI-Evidence-to-Decision-Simulator.
Upload your project files.
Add a README.md containing installation and running instructions.
Verify that the repository opens and the files are visible.
Copy the repository URL and submit it.

Important: Do not upload your .env file, API key, or .venv folder.

Option 2 — Submit through Google Drive

If the instructions specifically require a project folder or ZIP file, upload the ZIP to the provided Drive folder. You can also include your GitHub link in a text file.

Before you submit

Your project passed all 12 automated tests, which is a good sign. Keep app.py, evaluation.py, storage.py, sample_documents/, tests/, requirements.txt, and the other required project files in your repository.

One question

What exactly do the submission instructions say?

A. Submit the complete project folder through Google Drive.
B. Submit a GitHub repository link.
C. Submit either a Google Drive link or a GitHub link.
D. I'm not sure.

Reply with A, B, C, or D, and I'll guide you through the correct submission method.

I understand. From your screenshot, your sir has shared a Google Drive folder for the assignment and instructed students to share their assignment link in a Google Form. The assignment will be used to select students for an internship.

What should you submit?

My recommendation: Upload your complete project to GitHub, then submit its repository link through the Google Form, provided the form accepts GitHub URLs.

Follow these steps:

Create a GitHub repository named AI-Evidence-to-Decision-Simulator.
Upload your complete project source code, including app.py, evaluation.py, storage.py, sample_documents/, tests/, requirements.txt, and README.md.
Do not upload .env (it contains your API key), .venv/, or cache folders.
Open your GitHub repository and copy its URL.
Open the Google Form your sir shared and paste the repository URL into the assignment-link field.
Submit the form.

Your application has already passed 12 automated tests, so you're in a good position to prepare the submission.

One important thing

The screenshot mentions a Google Drive folder and a Google Form, but it doesn't show the actual form fields or whether GitHub links are accepted.

Please send me the Google Form link by opening it from your class message. I'll help you determine exactly what link and information you should submit.

# AI Evidence-to-Decision Simulator

A Streamlit application for the **provided internship assignment**. It investigates a synthetic shipment discrepancy involving 500 electronic components valued at ₹18,00,000. The scenario and assignment requirements have been preserved; the sample records are synthetic and do not accuse any real party.

## Windows setup using a virtual environment

Use the Python version installed on your machine (Python 3.10 is a good choice for this project). Open PowerShell in the extracted project folder:


powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py


If PowerShell says that py -3.10 is unavailable, use py -0p to list installed Python versions and replace 3.10 with an installed compatible version. In VS Code, choose .venv\Scripts\python.exe using **Python: Select Interpreter**. The .venv directory is intentionally not included in the ZIP; create it locally using the commands above.

To deactivate the environment later:


powershell
deactivate


## Optional OpenAI API integration

The app runs without an API key. Without one, the Q&A uses a conservative deterministic fallback and decision grading uses a transparent heuristic rubric. For LLM-powered evidence Q&A and criterion-level evaluation, set the key in the same PowerShell terminal before launching:


powershell
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_MODEL="gpt-4o-mini"
streamlit run app.py


Use an API key you are authorized to use; API usage may incur charges. Never commit the key or put it in source files. A missing key, API error, or invalid model response is handled with a fallback and visible notice.

## Features mapped to the assignment

- Case workspace and case summary.
- Extraction from PDF, .eml, .txt, .md, .csv, and .json records, including user-uploaded files.
- Stable evidence IDs, source filename, extraction method, and claim-status metadata.
- Searchable evidence register, heuristic date timeline, and rule-based conflict leads with source references.
- Evidence-grounded Q&A with structured JSON when the API is configured; citations are checked against currently released evidence IDs.
- Restricted synthetic records kept in hidden_records.json. Before release, only title/description are shown to the user and the hidden contents are not included in LLM prompts. A reason of at least 15 characters is required to request a record. Release and reason are recorded in local SQLite history.
- Decision form collecting conclusion, supporting evidence, counterevidence, confidence, reasoning, and next action.
- Criterion-level evaluation, Python validation of score schema/ranges/evidence references, and Python-calculated total out of 100. Evidence-presence caps stop the LLM from awarding high support/traceability scores when no relevant IDs are selected.
- Fallback rubric when LLM is unavailable. Fallback is heuristic and clearly labelled; do not represent it as expert human grading.
- Decision attempts, evidence-request history, released-record state, and Q&A history persisted in case_history.sqlite3 across app restarts for this local single-case training app.
- Attempt comparison and report export to Markdown and JSON.
- Tests for scoring bounds, invalid IDs, hidden evidence reference rejection, evidence-presence score caps, conflict-rule presence, and SQLite persistence.

## Run tests


powershell
python -m pytest -q


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

why rubrix in readme file delete these and tell about project only and install and it should be actractive  if any gif are avilable according to these project and i am using python 3.14

I've rewritten your README to make it more attractive, professional, and suitable for your internship assignment submission.

📄 Download your new README

Download the updated README.md

What I changed
❌ Removed the detailed evaluation rubric and scoring breakdown.
✅ Added a professional project introduction and description.
✨ Added an attractive feature list with icons.
🛠️ Listed the technologies used.
🐍 Updated installation instructions for Python 3.14 on Windows.
▶️ Included commands to install dependencies and run the Streamlit application.
📁 Added a project folder structure.
🔐 Included API-key security guidance.
📱 Improved the README's presentation for GitHub.
How to replace your existing README
Download the file above.
Open your project folder:
C:\Users\navee\OneDrive\Desktop\ai_evidence_simulator
Replace the existing README.md with the downloaded file.
Open it in VS Code and check the formatting.
Save it.
Can we add a GIF to make it more attractive?

Yes! A short demonstration GIF showing your actual application would look excellent on GitHub. For example, it could show the evidence register, conflict analysis, asking a question, and viewing the final report.

I haven't included a GIF because you haven't provided a recording of the application, and I don't want to add unrelated visuals that misrepresent your project.

My recommendation: First replace the README. Then we can create a GIF from your actual running application and add it near the top of the README. That will make your repository look more polished to the internship selection team.

README.md
Document

Library
/
README.md
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

An interactive project for evidence review, investigation, and structured decision support.
