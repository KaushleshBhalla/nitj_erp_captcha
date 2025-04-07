import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from io import BytesIO
import time

# -- USER DETAILS --
USERNAME = '23104045'
PASSWORD = 'K@ushlesh385'

# -- URLs --
BASE_URL = 'https://v1.nitj.ac.in/erp'
LOGIN_URL = BASE_URL + '/login'
CAPTCHA_URL = BASE_URL + '/cap.php'

# -- Max attempts --
MAX_ATTEMPTS = 5

# -- Start Session --
session = requests.Session()

def get_captcha_text():
    # Download CAPTCHA image
    captcha_img = session.get(CAPTCHA_URL)
    img = Image.open(BytesIO(captcha_img.content))

    # Preprocess for better OCR
    img = img.convert('L')  # grayscale
    # img = img.point(lambda x: 0 if x < 150 else 255, '1')  # optional binarization

    # Use pytesseract to read
    text = pytesseract.image_to_string(img).strip()
    return text

def attempt_login():
    # Load login page (for cookies/session)
    login_page = session.get(LOGIN_URL)
    soup = BeautifulSoup(login_page.text, 'html.parser')

    # Get captcha
    captcha_text = get_captcha_text()
    print(f"[+] CAPTCHA Solved: {captcha_text}")

    # Prepare payload
    payload = {
        'username': USERNAME,
        'pwd': PASSWORD,
        'captcha': captcha_text,
        'login': 'Login'
    }

    # Submit login form
    response = session.post(LOGIN_URL, data=payload)

    # Analyze response
    if 'user_home' in response.url or 'dashboard' in response.text:
        print("[✓] Login successful.")
        return True
    elif 'Invalid username or password' in response.text:
        print("[✗] Incorrect username or password.")
        return False
    elif 'Invalid Captcha' in response.text or 'captcha' in response.text.lower():
        print("[!] Captcha error — retrying...")
        return None
    else:
        print("[?] Unknown issue — saving response.")
        with open('debug.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        return False

# --- Main Loop ---
for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"\n[Attempt {attempt}] Trying to log in...")
    result = attempt_login()

    if result is True:
        break
    elif result is False:
        break
    else:
        time.sleep(1)  # brief delay before retry
else:
    print("failed login check your username and password")
