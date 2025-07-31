import json

def search_employees(employee_names, json_file="Safety courses.json"):
    """Search for specific employees in the Safety courses JSON file"""
    
    print(f"🔍 Searching for employees in {json_file}")
    print("=" * 60)
    
    try:
        # Load the JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"📊 Total employees in file: {len(data)}")
        print()
        
        found_employees = []
        
        for employee_name in employee_names:
            found = False
            for employee in data:
                if employee['name'].lower() == employee_name.lower():
                    found_employees.append(employee)
                    found = True
                    break
            
            if not found:
                print(f"❌ Employee not found: {employee_name}")
        
        # Display found employees
        for i, employee in enumerate(found_employees, 1):
            print(f"👤 Employee {i}: {employee['name']}")
            print(f"   📋 Code: {employee['code']}")
            print(f"   🏢 Department: {employee['department']}")
            print(f"   📚 Total Courses: {len(employee['courses'])}")
            
            print("   📖 Courses:")
            for j, course in enumerate(employee['courses'], 1):
                print(f"      {j}. {course['course_name']}")
                print(f"         📅 Course Date: {course['date_of_course']}")
                print(f"         ⏰ Expiry Date: {course['date_of_expiry']}")
            
            print()
        
        return found_employees
        
    except Exception as e:
        print(f"❌ Error reading file: {str(e)}")
        return []

def main():
    """Main function"""
    # List of employees to search for
    employee_names = [
        "Hany Mahmoud Mohamed",
        "Hassan Hosny Abd El Ghafar", 
        "Mohamed Ragab Ramadan",
        "Mohamed Sayed Gomaa",
        "Youssef Ramadan Khalil"
    ]
    
    # Search for employees
    found_employees = search_employees(employee_names)
    
    if found_employees:
        print(f"✅ Found {len(found_employees)} out of {len(employee_names)} employees")
    else:
        print("❌ No employees found")

if __name__ == "__main__":
    main() 