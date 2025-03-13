import json
import os
import runpod
from DOupload import uploadDO
from apply_mask import doCut
import requests
 
def handler(job):
    job_input = job['input']
    image_url = job_input.get('link')

    print("!!!", job.get('uploadTo'))

    if not image_url:
        return json.dumps({"error": "No image URL provided"}), 400
    
    uploadTo = job.get('uploadTo');
    if not uploadTo:
        return json.dumps({"error": "No upload creds"}), 400
    
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        os.makedirs('imgs', exist_ok=True)
        with open('imgs/downloaded.jpg', 'wb') as f:
            f.write(response.content)

        targetName = f'imgs/{uploadTo['object_name']}.png';
        doCut('imgs/downloaded.jpg', targetName)
        return uploadDO(targetName, uploadTo)
        

    except Exception as e:
        return json.dumps({"error": f"Failed to download image: {str(e)}"}), 500


def testHandler(job):
    return handler(job)


def test():
    # Call the handler function with the test image URL
    job = {
        'input': {
            'link': 'https://testitems.fra1.digitaloceanspaces.com/piz.jpg'
        },
        'uploadTo': {'region_name': 'fra1', 
                         'endpoint_url': 'https://fra1.digitaloceanspaces.com', 
                         'aws_access_key_id': 'DO00A68ZPATT2M7W6EJF', 
                         'aws_secret_access_key': '368lcCHa3Xff7LtmN1+Y8tc9p+Pw/86FwpZ507qx2V8', 
                         'bucket': 'rmbg', 
                         'object_name': 'lel2.jpg'}
    }

                
    return handler(job)

# test()
# 
runpod.serverless.start({"handler": handler})