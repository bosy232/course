import json

# قراءة ملف courses.json بدلاً من employees.json
with open('courses.json', 'r', encoding='utf-8') as f:
    employees = json.load(f)

merged = {}

for emp in employees:
    name = emp.get("Participant Name ", "").strip()
    code = emp.get("code", "")
    department = emp.get("Department", "")
    if not name:
        continue
    if name not in merged:
        merged[name] = {
            "name": name,
            "code": code,
            "department": department,
            "courses": []
        }
    merged[name]["courses"].append({
        "course_name": emp.get("Course Name", ""),
        "date_of_course": emp.get("Date of Course", ""),
        "date_of_expiry": emp.get("Date of Expiry", ""),
        "department": department
    })

merged_list = list(merged.values())

with open('merged_employees.json', 'w', encoding='utf-8') as f:
    json.dump(merged_list, f, ensure_ascii=False, indent=2)

print("تم إنشاء ملف merged_employees.json بنجاح!")
print(f"عدد الموظفين: {len(merged_list)}")
print(f"إجمالي عدد الدورات: {sum(len(emp['courses']) for emp in merged_list)}")