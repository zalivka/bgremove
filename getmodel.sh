#!/bin/bash

# Create directory if it doesn't exist
mkdir -p saved_models

# Download the model file
echo "Downloading model file..."
curl -L https://testitems.fra1.digitaloceanspaces.com/isnet.pth -o saved_models/isnet.pth

echo "Download complete!" 