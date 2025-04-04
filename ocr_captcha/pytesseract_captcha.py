import cv2
import pytesseract
import numpy as np
import os

# Configure Tesseract to recognize only digits
custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

def preprocess_image(image_path):
    """Preprocess image for better OCR accuracy."""
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: File not found -> {image_path}")
        return None

    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        print(f"Error: OpenCV cannot read the image at {image_path}")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Morphological operations
    kernel = np.ones((2,2), np.uint8)
    processed_image = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    
    return processed_image

def solve_captcha(image_path):
    """Recognize numeric CAPTCHA using Tesseract OCR."""
    processed_image = preprocess_image(image_path)
    if processed_image is None:
        return "Error in processing CAPTCHA"

    # Use Tesseract OCR to extract digits
    captcha_text = pytesseract.image_to_string(processed_image, config=custom_config)
    
    return captcha_text.strip()

# Define correct file paths
captcha_1 = r"C:\Users\HP\Desktop\nitj_erp_captcha\100captcha_requests\captcha_1.jpg"
captcha_2 = r"C:\Users\HP\Desktop\nitj_erp_captcha\100captcha_requests\captcha_2.jpg"

# Print paths for debugging
print(f"Processing: {captcha_1}")
print(f"Processing: {captcha_2}")

# Solve CAPTCHAs
print("CAPTCHA 1:", solve_captcha(captcha_1))
print("CAPTCHA 2:", solve_captcha(captcha_2))
