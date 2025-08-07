import json

def compare_employees():
    print("🔍 مقارنة الموظفين بين الملفين")
    print("=" * 60)
    
    # قراءة الملفين
    with open('merged_employees.json', 'r', encoding='utf-8') as f:
        merged_employees = json.load(f)
    
    with open('Safety courses.json', 'r', encoding='utf-8') as f:
        safety_employees = json.load(f)
    
    # إنشاء قوائم الأسماء والأكواد
    merged_names = {emp['name']: emp['code'] for emp in merged_employees}
    merged_codes = {emp['code']: emp['name'] for emp in merged_employees}
    
    safety_names = {emp['name']: emp['code'] for emp in safety_employees}
    safety_codes = {emp['code']: emp['name'] for emp in safety_employees}
    
    print(f"📊 إحصائيات الملفين:")
    print(f"   merged_employees.json: {len(merged_employees)} موظف")
    print(f"   Safety courses.json: {len(safety_employees)} موظف")
    print()
    
    # التحقق من وجود موظفي Safety في merged
    missing_in_merged = []
    found_in_merged = []
    
    for safety_emp in safety_employees:
        safety_name = safety_emp['name']
        safety_code = safety_emp['code']
        
        if safety_name in merged_names:
            merged_code = merged_names[safety_name]
            if safety_code == merged_code:
                found_in_merged.append({
                    'name': safety_name,
                    'code': safety_code,
                    'status': '✅ موجود بنفس الكود'
                })
            else:
                found_in_merged.append({
                    'name': safety_name,
                    'code': safety_code,
                    'merged_code': merged_code,
                    'status': '⚠️ موجود بكود مختلف'
                })
        elif safety_code in merged_codes:
            merged_name = merged_codes[safety_code]
            found_in_merged.append({
                'name': safety_name,
                'code': safety_code,
                'merged_name': merged_name,
                'status': '⚠️ موجود بنفس الكود ولكن اسم مختلف'
            })
        else:
            missing_in_merged.append({
                'name': safety_name,
                'code': safety_code,
                'status': '❌ غير موجود'
            })
    
    # التحقق من وجود موظفي merged في Safety
    missing_in_safety = []
    for merged_emp in merged_employees:
        merged_name = merged_emp['name']
        merged_code = merged_emp['code']
        
        if merged_name not in safety_names and merged_code not in safety_codes:
            missing_in_safety.append({
                'name': merged_name,
                'code': merged_code,
                'status': '❌ غير موجود في Safety'
            })
    
    # عرض النتائج
    print("📋 نتائج المقارنة:")
    print("=" * 60)
    
    print(f"\n✅ الموظفون الموجودون في merged_employees.json:")
    for emp in found_in_merged:
        if emp['status'] == '✅ موجود بنفس الكود':
            print(f"   ✅ {emp['name']} - {emp['code']}")
        elif 'merged_code' in emp:
            print(f"   ⚠️ {emp['name']} - Safety: {emp['code']}, Merged: {emp['merged_code']}")
        elif 'merged_name' in emp:
            print(f"   ⚠️ {emp['name']} - Safety: {emp['code']}, Merged Name: {emp['merged_name']}")
    
    if missing_in_merged:
        print(f"\n❌ الموظفون المفقودون من merged_employees.json:")
        for emp in missing_in_merged:
            print(f"   ❌ {emp['name']} - {emp['code']}")
    
    if missing_in_safety:
        print(f"\n❌ الموظفون المفقودون من Safety courses.json:")
        for emp in missing_in_safety:
            print(f"   ❌ {emp['name']} - {emp['code']}")
    
    # الإحصائيات النهائية
    print(f"\n📊 الإحصائيات النهائية:")
    print("=" * 60)
    print(f"✅ موجودون بنفس الكود: {len([e for e in found_in_merged if e['status'] == '✅ موجود بنفس الكود'])}")
    print(f"⚠️ موجودون بكود مختلف: {len([e for e in found_in_merged if 'merged_code' in e])}")
    print(f"⚠️ موجودون باسم مختلف: {len([e for e in found_in_merged if 'merged_name' in e])}")
    print(f"❌ مفقودون من merged: {len(missing_in_merged)}")
    print(f"❌ مفقودون من Safety: {len(missing_in_safety)}")
    
    # التحقق النهائي
    total_safety = len(safety_employees)
    found_total = len([e for e in found_in_merged if e['status'] == '✅ موجود بنفس الكود'])
    
    print(f"\n🎯 النتيجة النهائية:")
    if found_total == total_safety:
        print("✅ جميع موظفي Safety courses موجودون في merged_employees.json")
    else:
        print(f"❌ {total_safety - found_total} موظف من Safety courses غير موجودين في merged_employees.json")
    
    return found_in_merged, missing_in_merged, missing_in_safety

if __name__ == "__main__":
    compare_employees() 