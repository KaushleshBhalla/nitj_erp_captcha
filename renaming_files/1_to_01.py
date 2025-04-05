import os

image_folder = R"C:\Users\HP\Desktop\nitj_erp_captcha\captcha_100_requests\captchas100"  # Raw string for path

for i in range(1, 101):
    old_filename = f"captcha_{i}.jpg"  # Assuming they are all .jpg (change if needed)
    new_filename = f"captcha_{i:02}.jpg"  # Formats number with leading zero

    old_path = os.path.join(image_folder, old_filename)
    new_path = os.path.join(image_folder, new_filename)

    if os.path.exists(old_path):  # Check if the file exists before renaming
        os.rename(old_path, new_path)
        print(f"Renamed '{old_filename}' to '{new_filename}'")
    else:
        print(f"File '{old_filename}' not found.")

print("Renaming process completed.")