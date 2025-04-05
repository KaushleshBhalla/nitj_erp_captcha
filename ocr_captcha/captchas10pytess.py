from PIL import Image
import pytesseract
import os

image_folder = R"C:\Users\HP\Desktop\nitj_erp_captcha\captcha_100_requests\captchas10"
output_file = R"C:\Users\HP\Desktop\nitj_erp_captcha\captcha_10_solutions.txt"


with open(output_file, 'w') as f:
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            try:
                img = Image.open(image_path)
                text = pytesseract.image_to_string(img, config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789')
                
                cleaned_text = text.strip()
                f.write(f"{filename},{cleaned_text}\n")
                print(f"Processed {filename}: {cleaned_text}")
            except Exception as e:
                f.write(f"{filename},ERROR\n")
                print(f"Error processing {filename}: {e}")

print(f"\nOCR results saved to {output_file}")