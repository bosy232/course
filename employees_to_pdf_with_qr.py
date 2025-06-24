import json
from fpdf import FPDF
import qrcode
import os

# استخدم رابط اللوكل هوست
BASE_URL = "http://localhost:3000/employee/"

with open('merged_employees.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=14)

for emp in employees:
    name = emp.get("name", "").strip()
    code = emp.get("code", "")
    if not code:
        continue

    # توليد رابط الموظف
    url = f"{BASE_URL}{code}"

    # توليد QR code وحفظه كصورة مؤقتة
    qr_img_path = f"qr_{code}.png"
    qr = qrcode.make(url)
    qr.save(qr_img_path)

    pdf.add_page()
    pdf.cell(0, 10, f"Name: {name}", ln=True)
    pdf.cell(0, 10, f"Profile Link: {url}", ln=True)
    pdf.image(qr_img_path, x=10, y=30, w=50, h=50)
    pdf.ln(60)
    pdf.cell(0, 10, "Courses:", ln=True)
    pdf.set_font("Arial", size=11)
    for course in emp.get("courses", []):
        pdf.cell(0, 10, f"    - {course['course_name']} ({course['date_of_course']} - {course['date_of_expiry']})", ln=True)
    pdf.set_font("Arial", size=14)

    # حذف صورة QR المؤقتة بعد إضافتها للـ PDF
    os.remove(qr_img_path)

pdf.output("employees_qr_codes.pdf")
print("تم إنشاء ملف employees_qr_codes.pdf بنجاح!")