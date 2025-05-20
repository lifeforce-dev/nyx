@echo off
REM Create venv if not already present
if not exist venv (
    py -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Upgrade pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -e .

echo Environment setup complete.
pause
