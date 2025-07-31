import json

def add_safety_employees_to_merged():
    """Add Safety course employees to merged_employees.json"""
    
    print("🔄 Adding Safety course employees to merged_employees.json")
    print("=" * 60)
    
    try:
        # Load Safety courses data
        print("📖 Loading Safety courses data...")
        with open("Safety courses.json", 'r', encoding='utf-8') as f:
            safety_data = json.load(f)
        
        # Load existing merged employees data
        print("📖 Loading existing merged_employees.json...")
        with open("merged_employees.json", 'r', encoding='utf-8') as f:
            merged_data = json.load(f)
        
        print(f"📊 Current employees in merged_employees.json: {len(merged_data)}")
        print(f"📊 Safety course employees: {len(safety_data)}")
        
        # List of employees to add
        employees_to_add = [
            "Hany Mahmoud Mohamed",
            "Hassan Hosny Abd El Ghafar", 
            "Mohamed Ragab Ramadan",
            "Mohamed Sayed Gomaa",
            "Youssef Ramadan Khalil"
        ]
        
        # Find employees in Safety data
        found_employees = []
        for employee_name in employees_to_add:
            for employee in safety_data:
                if employee['name'].lower() == employee_name.lower():
                    found_employees.append(employee)
                    break
        
        print(f"✅ Found {len(found_employees)} employees to add")
        
        # Check if employees already exist in merged data
        existing_names = [emp['name'].lower() for emp in merged_data]
        new_employees = []
        
        for employee in found_employees:
            if employee['name'].lower() not in existing_names:
                new_employees.append(employee)
                print(f"➕ Adding: {employee['name']}")
            else:
                print(f"⚠️  Already exists: {employee['name']}")
        
        # Add new employees to merged data
        if new_employees:
            merged_data.extend(new_employees)
            
            # Save updated merged data
            with open("merged_employees.json", 'w', encoding='utf-8') as f:
                json.dump(merged_data, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ Successfully added {len(new_employees)} new employees!")
            print(f"📊 Total employees now: {len(merged_data)}")
            
            # Show summary of added employees
            print(f"\n📋 Added employees:")
            for i, emp in enumerate(new_employees, 1):
                print(f"   {i}. {emp['name']} ({emp['department']}) - {len(emp['courses'])} courses")
            
        else:
            print(f"\n⚠️  No new employees to add (all already exist)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    """Main function"""
    success = add_safety_employees_to_merged()
    
    if success:
        print(f"\n🎉 Operation completed successfully!")
    else:
        print(f"\n💥 Operation failed!")

if __name__ == "__main__":
    main() 