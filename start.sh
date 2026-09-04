#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

# Add portable node tools to PATH if present
if [ -d "$DIR/.tools/node/bin" ]; then
    export PATH="$DIR/.tools/node/bin:$PATH"
fi

echo "================================================================="
echo "🌿 Starting SIH 2024 PS 26044: AYUSH Academia-Industry Portal"
echo "================================================================="

# Activate virtual environment
if [ -d "backend/venv" ]; then
    source backend/venv/bin/activate
fi

# Run backend test suite to ensure health
python backend/test_api.py

echo "Starting unified web server on http://127.0.0.1:5000 ..."
python run.py
