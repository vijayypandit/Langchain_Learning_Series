#!/bin/bash

# YouTube Video Chat - Setup Script
# This script helps set up the environment

echo ""
echo "===================================="
echo "YouTube Video Chat - Setup"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[1/4] Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo "[2/4] Checking for .env file..."
if [ ! -f .env ]; then
    echo "[3/4] Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env and add your API keys"
    if command -v nano &> /dev/null; then
        nano .env
    elif command -v vi &> /dev/null; then
        vi .env
    fi
else
    echo "[3/4] .env file already exists"
fi

echo "[4/4] Setup complete!"
echo ""
echo "To start the app, run:"
echo "  streamlit run app.py"
echo ""
