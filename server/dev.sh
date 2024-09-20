#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Set up virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
if command_exists "source"; then
    source venv/bin/activate
else
    echo "Error: 'source' command not found. Please ensure you are using Bash or Zsh."
    exit 1
fi

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found. Skipping installation."
fi

# Export environment variables from .env if it exists
if [ -f ".env" ]; then
    echo "Loading environment variables from .env file..."
    export $(grep -v '#' .env | xargs)
else
    echo "No .env file found. Skipping environment variable loading."
fi

# Run FastAPI app using Uvicorn
echo "Starting FastAPI server..."
if command_exists "uvicorn"; then
    uvicorn app.main:app --reload
else
    echo "Error: 'uvicorn' command not found. Please install it and ensure it is in your PATH."
    exit 1
fi
