print("🚀 Script Started")

import os
import requests

FOLDER = "C:\\Users\\HP\\Desktop\\nitj_erp_captcha\\100captcha_requests\\captchas100\\"
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)
    print("✅ Folder Created:", FOLDER)
else:
    print("📂 Folder Already Exists:", FOLDER)

CAPTCHA_URL = "https://v1.nitj.ac.in/erp/cap.php"


for i in range(100):
    response = requests.get(CAPTCHA_URL)
    if response.status_code == 200:
        file_name = FOLDER + str('captcha_') + str(i+1) + str('.jpg')
        with open(file_name,"wb") as file:
            file.write(response.content)
        print('saved'+ file_name)
        #print(f"✅ Saved: {file_name}")  # Print success message
    else:
        print("failed" + file_name)
        #print(f"❌ Failed to download CAPTCHA {i+1}")  # Print error if failed