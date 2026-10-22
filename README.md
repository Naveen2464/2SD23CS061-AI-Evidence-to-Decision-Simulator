# 🚀 AI Evidence-to-Decision Simulator

**Transform case documents into structured, evidence-based investigations.**

AI Evidence-to-Decision Simulator is an interactive web application built with Python and Streamlit. It helps users examine case documents, identify conflicting information, trace claims to their sources, investigate missing evidence, and prepare structured decisions.

The application demonstrates how AI-assisted analysis can support investigative workflows while maintaining transparency, evidence traceability, and responsible decision-making.

---

## ✨ Key Features

📁 **Document Analysis**
Review case documents and extract information from supported file formats.

🔎 **Evidence Register**
Search evidence records, inspect source information, and reference evidence using unique IDs.

🧭 **Timeline & Conflict Detection**
Explore event dates, identify potential inconsistencies, and investigate conflicting claims.

💬 **AI-Powered Investigation**
Ask questions about the case and receive evidence-oriented responses with citations when available.

🔐 **Controlled Evidence Requests**
Request restricted records with a reason and track record releases in the application's history.

📝 **Decision Workspace**
Prepare structured conclusions with supporting evidence, counterevidence, confidence levels, reasoning, and recommended actions.

📊 **Decision Analysis**
Receive feedback on the reasoning and evidence used in a submitted decision.

💾 **Persistent Case History**
Store investigation activity and decision attempts locally using SQLite.

📄 **Report Export**
Export the investigation report in Markdown format and the case state in JSON format.

---

## 🖥️ Technology Stack

* **Language:** Python 3.14
* **Web Framework:** Streamlit
* **Database:** SQLite
* **Testing:** Pytest
* **AI Integration:** Configured AI provider, with fallback behavior where supported
* **Data Formats:** PDF, EML, TXT, Markdown, CSV, and JSON

---

## 📸 Application Preview

The application provides an interactive workspace for reviewing evidence, investigating discrepancies, asking questions, and preparing a final report.

> *Add a GIF or screenshot of the actual running application here to give visitors a visual preview.*

---

## ⚙️ Installation and Setup

### Prerequisites

* Windows 10 or Windows 11
* Python 3.14
* Git (optional, for cloning the repository)

### 1. Clone the repository

If the project is hosted on GitHub, open PowerShell and run:

```powershell
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the downloaded project folder:

```powershell
cd ai_evidence_simulator
```

Replace the repository URL with your actual GitHub repository URL.

If you already have the project folder, open PowerShell in that folder instead.

### 2. Create a virtual environment

```powershell
py -3.14 -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Launch the application

```powershell
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

`http://localhost:8501`

### 6. Run the automated tests

```powershell
python -m pytest -v
```

---

## 🔍 Example Use Case

The demonstration case concerns a shipment of electronic components.

* **Ordered quantity:** 500 units
* **Order value:** ₹18,00,000
* **Warehouse count:** 420 units
* **Reported discrepancy:** 80 units

The application allows investigators to compare purchase orders, supplier communications, carrier tracking, warehouse records, packing slips, and address-change communications.

It helps identify what the available evidence supports, what remains uncertain, and which additional records should be obtained.

The application does not automatically assign blame or infer fraud from an unresolved discrepancy.

---

## 🔐 Security and Responsible Use

* The demonstration uses fictional parties and synthetic records.
* Document contents are treated as evidence, not as instructions to the application.
* API keys and other secrets must never be committed to GitHub.
* The local SQLite database is intended for a single-case training application.
* Potential conflicts and timeline findings should be verified against their original source documents.

---

## 📂 Project Structure

```text
ai_evidence_simulator/
│
├── app.py
├── evaluation.py
├── storage.py
├── hidden_records.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── sample_documents/
│
└── tests/
```

The application may also create local database and cache files when it runs.

---

## 👨‍💻 Project Purpose

This project demonstrates the development of an interactive investigation tool combining document processing, evidence traceability, AI-assisted question answering, conflict analysis, persistent storage, and structured decision support.

**Built with Python and Streamlit.**
