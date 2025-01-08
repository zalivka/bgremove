#!/bin/bash

# Create directory if it doesn't exist
mkdir -p saved_models

# Download the model file
echo "Downloading model file..."
curl -L https://testitems.fra1.digitaloceanspaces.com/isnet.pth -o saved_models/isnet.pth

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
