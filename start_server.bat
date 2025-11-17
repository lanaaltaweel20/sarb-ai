@echo off
echo Starting SARB AI API Server...
python -m uvicorn main:app --reload
pause