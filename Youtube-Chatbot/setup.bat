@echo off
REM YouTube Video Chat - Setup Script
REM This script helps set up the environment

echo.
echo ====================================
echo YouTube Video Chat - Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [2/4] Checking for .env file...
if not exist .env (
    echo [3/4] Creating .env file from template...
    copy .env.example .env
    echo Please edit .env and add your API keys
    echo Opening .env in notepad...
    notepad .env
) else (
    echo [3/4] .env file already exists
)

echo [4/4] Setup complete!
echo.
echo To start the app, run:
echo   streamlit run app.py
echo.
pause
