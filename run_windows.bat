@echo off
setlocal
if not exist .venv\Scripts\python.exe (
  echo Creating local virtual environment with Python 3.10...
  py -3.10 -m venv .venv
  if errorlevel 1 (
    echo Could not find Python 3.10. Run py -0p and edit this script to use an installed compatible version.
    pause
    exit /b 1
  )
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 pause & exit /b 1
streamlit run app.py
endlocal
