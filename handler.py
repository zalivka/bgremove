import os
import runpod
from flask import Flask, request, jsonify

from apply_mask import doCut

import requests

# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.


def handler(job):
    """ Handler function that will be used to process jobs. """
    job_input = job['input']
    
    # Get image URL from job input
    image_url = job_input.get('link')
    if not image_url:
        return {"error": "No image URL provided"}
        
    # Download image from URL
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        
        # Create imgs directory if it doesn't exist
        os.makedirs('imgs', exist_ok=True)
        # Save downloaded image
        with open('imgs/downloaded.jpg', 'wb') as f:
            f.write(response.content)

        doCut('imgs/downloaded.jpg')

        with open('res/applied.png', 'rb') as f:
            result_image = f.read()

        return result_image, 200, {'Content-Type': 'image/jpg'}
    except Exception as e:
        return {"error": f"Failed to download image: {str(e)}"}




runpod.serverless.start({"handler": handler})