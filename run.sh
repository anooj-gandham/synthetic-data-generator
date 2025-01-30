#!/bin/bash

# Function to clean up child processes
cleanup() {
  echo "Stopping processes..."
  pkill -P $$  # Kill all child processes of this script
  exit 0
}

# Trap SIGINT (Ctrl + C) and call cleanup
trap cleanup SIGINT

source .env

# Start Flask Backend
echo "Starting backend..."
python ./backend/run.py &

# Use watchdog to monitor only interface.py for changes
echo "Starting frontend with Watchdog..."
watchmedo auto-restart --patterns="interface.py" --recursive -- python ./frontend/interface.py &

# Wait for all child processes
wait
