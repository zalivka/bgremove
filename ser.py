from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from apply_mask import doCut
from run import run_inference

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'imgs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return "kek"


@app.route('/bg', methods=['POST'])
def remove_background():
    # Check if image file is present in request
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
            doCut(filepath)
            # Return the processed image file
            with open('res/applied.png', 'rb') as f:
                result_image = f.read()
            return result_image, 200, {'Content-Type': 'image/png'}
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
