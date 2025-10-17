@echo off
echo ============================================================
echo   YOLOv5 Web App - Google Cloud Run Deployment
echo ============================================================
echo.

echo Step 1: Checking gcloud installation...
where gcloud >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: gcloud CLI not found!
    echo Please install from: https://cloud.google.com/sdk/docs/install
    pause
    exit /b 1
)
echo ✓ gcloud CLI found

echo.
echo Step 2: Logging in to Google Cloud...
call gcloud auth login

echo.
echo Step 3: Setting project...
set /p PROJECT_ID="Enter your Google Cloud Project ID: "
call gcloud config set project %PROJECT_ID%

echo.
echo Step 4: Enabling required APIs...
call gcloud services enable cloudbuild.googleapis.com
call gcloud services enable run.googleapis.com
call gcloud services enable containerregistry.googleapis.com

echo.
echo Step 5: Deploying to Cloud Run...
echo This may take 5-10 minutes...
call gcloud run deploy yolov5-webapp --source . --region us-central1 --platform managed --allow-unauthenticated --memory 2Gi --cpu 2 --timeout 300 --max-instances 10

echo.
echo ============================================================
echo   Deployment Complete!
echo ============================================================
echo.
echo Your app is now live! Get the URL with:
echo gcloud run services describe yolov5-webapp --region us-central1 --format "value(status.url)"
echo.
pause
