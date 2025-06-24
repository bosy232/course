<<<<<<< HEAD
import json
import qrcode
import os
import re

BASE_URL = "http://localhost:3000/employee/"
QR_DIR = "qr_codes"
os.makedirs(QR_DIR, exist_ok=True)

with open('merged_employees.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)

for emp in employees:
    name = emp.get("name", "").strip()
    code = emp.get("code", "")
    if not code or not name:
        continue

    url = f"{BASE_URL}{code}"
    safe_name = re.sub(r'[^A-Za-z0-9_\- ]', '', name).replace(" ", "_")
    filename = f"{safe_name}.png"
    filepath = os.path.join(QR_DIR, filename)

    qr = qrcode.make(url)
    qr.save(filepath)

=======
import json
import qrcode
import os
import re

BASE_URL = "http://localhost:3000/employee/"
QR_DIR = "qr_codes"
os.makedirs(QR_DIR, exist_ok=True)

with open('merged_employees.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)

for emp in employees:
    name = emp.get("name", "").strip()
    code = emp.get("code", "")
    if not code or not name:
        continue

    url = f"{BASE_URL}{code}"
    safe_name = re.sub(r'[^A-Za-z0-9_\- ]', '', name).replace(" ", "_")
    filename = f"{safe_name}.png"
    filepath = os.path.join(QR_DIR, filename)

    qr = qrcode.make(url)
    qr.save(filepath)

>>>>>>> 5736c5ba0be12afe508f50f6fda9bf4c6c2fd184
print(f"تم حفظ جميع QR codes في مجلد {QR_DIR} (واحد لكل موظف).")