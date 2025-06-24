import json
import qrcode
import os
import re

# استخدم رابط اللوكل هوست
BASE_URL = "http://localhost:3000/employee/"

# اسم المجلد الذي سيتم حفظ QR codes فيه
QR_DIR = "qr_codes"

# إنشاء المجلد إذا لم يكن موجودًا
os.makedirs(QR_DIR, exist_ok=True)

with open('merged_employees.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)

for emp in employees:
    name = emp.get("name", "").strip()
    code = emp.get("code", "")
    if not code or not name:
        continue

    # توليد رابط الموظف
    url = f"{BASE_URL}{code}"

    # تنظيف اسم الموظف ليكون صالح كاسم ملف
    safe_name = re.sub(r'[^A-Za-z0-9_\- ]', '', name).replace(" ", "_")
    filename = f"{safe_name}.png"
    filepath = os.path.join(QR_DIR, filename)

    # توليد QR code وحفظه
    qr = qrcode.make(url)
    qr.save(filepath)

print(f"تم حفظ جميع QR codes في مجلد {QR_DIR} (واحد لكل موظف).")