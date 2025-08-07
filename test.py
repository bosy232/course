import json

# 1. قراءة الملف الأساسي (merged_employees.json)
try:
    with open('merged_employees.json', 'r', encoding='utf-8') as file:
        merged_employees = json.load(file)
except FileNotFoundError:
    merged_employees = []

# 2. قراءة ملف Safety (Safety courses 2025 Jan to June 2025.json)
with open('Safety courses 2025 Jan to June 2025.json', 'r', encoding='utf-8') as file:
    safety_courses = json.load(file)

# 3. استخراج الأكواد من الملف الأساسي
existing_codes = {employee.get('code') for employee in merged_employees if 'code' in employee}

# 4. تحديد الموظفين الموجودين في Safety وغير موجودين في الملف الأساسي
missing_employees = [
    employee for employee in safety_courses
    if employee.get('code') and employee.get('code') not in existing_codes
]

# 5. عرض النتائج مع الاسم والكود
if missing_employees:
    print("الموظفون الموجودون في ملف Safety وغير موجودين في الملف الأساسي:")
    for idx, employee in enumerate(missing_employees, 1):
        name = employee.get("Safety Courses 2025 \n Jan- June 2025", "غير محدد")
        code = employee.get('code', "غير معروف")
        print(f"{idx}. الاسم: {name} | الكود: {code}")
else:
    print("لا يوجد موظفين في ملف Safety غير موجودين في الملف الأساسي.")