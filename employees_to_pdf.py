<<<<<<< HEAD
import json
from fpdf import FPDF

# تحميل بيانات الموظفين من الملف الجديد
with open('merged_employees.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)

# إنشاء ملف PDF جديد
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=14)

pdf.cell(0, 10, "Employees and Codes", ln=True, align='C')
pdf.ln(10)

for emp in employees:
    name = emp.get("name", "").strip()
    code = emp.get("code", "")
    pdf.cell(0, 10, f"Name: {name}    |    Code: {code}", ln=True)
    # عرض جميع الكورسات
    for course in emp.get("courses", []):
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 10, f"    - {course['course_name']} ({course['date_of_course']} - {course['date_of_expiry']})", ln=True)
    pdf.set_font("Arial", size=14)
    pdf.ln(5)

# حفظ الملف
pdf.output("employees_codes.pdf")
=======
import json
from fpdf import FPDF

# تحميل بيانات الموظفين من الملف الجديد
with open('merged_employees.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)

# إنشاء ملف PDF جديد
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=14)

pdf.cell(0, 10, "Employees and Codes", ln=True, align='C')
pdf.ln(10)

for emp in employees:
    name = emp.get("name", "").strip()
    code = emp.get("code", "")
    pdf.cell(0, 10, f"Name: {name}    |    Code: {code}", ln=True)
    # عرض جميع الكورسات
    for course in emp.get("courses", []):
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 10, f"    - {course['course_name']} ({course['date_of_course']} - {course['date_of_expiry']})", ln=True)
    pdf.set_font("Arial", size=14)
    pdf.ln(5)

# حفظ الملف
pdf.output("employees_codes.pdf")
>>>>>>> 5736c5ba0be12afe508f50f6fda9bf4c6c2fd184
print("تم إنشاء ملف employees_codes.pdf بنجاح!")