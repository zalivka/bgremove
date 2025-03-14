from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from apply_mask import doCut
import handler
from run import run_inference
import setproctitle
import tracemalloc

tracemalloc.start()
setproctitle.setproctitle("bgremove")

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'imgs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/bg', methods=['GET'])
def ping():
    return "ok", 200

@app.route('/test', methods=['POST'])
def test():
    # Call the handler function with the test image URL
    job = {
        'input': {
            'link': 'https://testitems.fra1.digitaloceanspaces.com/hu.jpg'
        }
    }
    return handler.handler(job)

   
@app.route('/bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['image']
    
    # Check if file is selected
    if file.filename == '':
        print("No selected file")
        return jsonify({'error': 'No selected file'}), 400
        
    if file and allowed_file(file.filename):
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Process image using existing run_inference
        try:
            import psutil
            process = psutil.Process()
            mem_before = process.memory_info().rss / 1024 / 1024  # Memory in MB
            cpu_before = psutil.cpu_percent()
            
            doCut(filepath, 'res/applied.png')
            
            mem_after = process.memory_info().rss / 1024 / 1024
            cpu_after = psutil.cpu_percent()
            
            print(f"Memory usage: {mem_after - mem_before:.2f} MB")
            print(f"CPU usage: {cpu_after - cpu_before:.2f}%")

            # Return the processed image file
            with open('res/applied.png', 'rb') as f:
                result_image = f.read()
    
            return result_image, 200, {'Content-Type': 'image/png'}
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400


@app.route('/bgtest', methods=['POST'])
def testcred():
    # Get JSON data from the request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    # Create a job object from the request data
    job = {
        'input': data.get('input', {}),
        'uploadTo': data.get('uploadTo', {})
    }
    
    # Validate required fields
    if not job['input'].get('link'):
        return jsonify({"error": "No image URL provided in input"}), 400
    
    if not job['uploadTo']:
        return jsonify({"error": "No upload credentials provided"}), 400
        
    return handler.testHandler(job)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    # app.run(debug=True, port=5000)
    
