@echo off
title Starting StudyPilot AI...
echo ========================================================
echo           Launching StudyPilot AI Web App
echo ========================================================
echo.

set PATH=C:\Program Files\nodejs;%PATH%
set DIR=%~dp0

echo 1. Starting FastAPI Backend Server on port 8000...
start "StudyPilot Backend" cmd /k "cd /d %DIR%backend && python -m uvicorn main:app --host 127.0.0.1 --port 8000"

echo 2. Starting Vite Frontend Server on port 5173...
start "StudyPilot Frontend" cmd /k "cd /d %DIR%frontend && npm run dev"

echo 3. Opening Web App in Browser...
timeout /t 3 >nul
start http://localhost:5173

echo.
echo ========================================================
echo StudyPilot AI is running! Keep the open command windows running.
echo ========================================================
