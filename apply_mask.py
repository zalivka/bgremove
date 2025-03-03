import numpy as np
from PIL import Image
import os
from run import run_inference 

def doCut(source_img, target_img):
    # Check if image is RGBA and convert to RGB if needed
    img = Image.open(source_img)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
        img.save(source_img)
    run_inference(source_img)

    # Create output directory if it doesn't exist
    os.makedirs('res', exist_ok=True)

    # Load the color image and mask
    img = Image.open(source_img)
    mask = Image.open('res/mask.png').convert('L')  # Convert mask to grayscale

    # Convert to numpy arrays
    img_array = np.array(img)
    mask_array = np.array(mask)

    # Normalize mask to 0-1 range
    mask_array = mask_array / 255.0

    # Apply mask by multiplying each color channel
    result = img_array.copy()
    for c in range(3):  # Apply to each RGB channel
        result[:,:,c] = img_array[:,:,c] * mask_array

    # Convert to RGBA by adding alpha channel from mask
    rgba = np.zeros((img_array.shape[0], img_array.shape[1], 4), dtype=np.uint8)
    rgba[:,:,:3] = result
    rgba[:,:,3] = (mask_array * 255).astype(np.uint8)  # Alpha channel from mask

    # Convert back to PIL Image and save as PNG with transparency
    result_img = Image.fromarray(rgba)
    result_img.save(target_img, format='PNG')