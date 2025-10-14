@echo off
echo ============================================================
echo YOLOv5 Object Detection Web Application
echo ============================================================
echo.
echo Starting the web server...
echo.
echo Once started, open your browser and go to:
echo http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ============================================================
echo.

REM Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    python app.py
) else (
    python app.py
)

pause
