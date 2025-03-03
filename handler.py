import os
import runpod
from flask import Flask, request, jsonify, send_file

from DOupload import upload_to_do
from apply_mask import doCut
# from run import run_inference

import requests

# If your handler runs inference on a model, load the model here.
#!!! # You will want models to be loaded into memory before starting serverless.



def handler(job):
    """ Handler function that will be used to process jobs. """
    job_input = job['input']
    
    # Get image URL from job input
    image_url = job_input.get('link')
    if not image_url:
        return jsonify({"error": "No image URL provided"}), 400
        
    # Download image from URL
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        
        # Create imgs directory if it doesn't exist
        os.makedirs('imgs', exist_ok=True)
        # Save downloaded image
        with open('imgs/downloaded.jpg', 'wb') as f:
            f.write(response.content)

        doCut('imgs/downloaded.jpg', 'res/applied.png')
        return upload_to_do('res/applied.png')
        

    except Exception as e:
        return jsonify({"error": f"Failed to download image: {str(e)}"}), 500

def test():
    # Call the handler function with the test image URL
    job = {
        'input': {
            'link': 'https://testitems.fra1.digitaloceanspaces.com/piz.jpg'
        }
    }
    return handler(job)

# test()
# 
runpod.serverless.start({"handler": handler})