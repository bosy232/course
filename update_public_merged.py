import json
import shutil

def update_public_merged_file():
    """Update public/merged_employees.json with Safety course employees"""
    
    print("🔄 Updating public/merged_employees.json with Safety course employees")
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
        
        # Create a combined list
        combined_data = merged_data.copy()
        
        # Add Safety course employees (avoiding duplicates)
        existing_names = [emp['name'].lower() for emp in combined_data]
        added_count = 0
        
        for safety_emp in safety_data:
            if safety_emp['name'].lower() not in existing_names:
                combined_data.append(safety_emp)
                added_count += 1
                print(f"➕ Added: {safety_emp['name']} ({safety_emp['code']})")
        
        print(f"\n✅ Added {added_count} new employees from Safety courses")
        print(f"📊 Total employees now: {len(combined_data)}")
        
        # Save to public/merged_employees.json
        print("💾 Saving to public/merged_employees.json...")
        with open("public/merged_employees.json", 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, ensure_ascii=False, indent=2)
        
        # Also update the main merged_employees.json
        print("💾 Updating main merged_employees.json...")
        with open("merged_employees.json", 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Successfully updated both files!")
        
        # Show some statistics
        print(f"\n📈 Final Statistics:")
        print(f"   - Total employees: {len(combined_data)}")
        
        # Count courses
        total_courses = sum(len(emp['courses']) for emp in combined_data)
        print(f"   - Total courses: {total_courses}")
        
        # Count departments
        departments = set(emp['department'] for emp in combined_data)
        print(f"   - Departments: {list(departments)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    """Main function"""
    success = update_public_merged_file()
    
    if success:
        print(f"\n🎉 Update completed successfully!")
        print(f"🌐 The website should now work with all Safety course employees")
    else:
        print(f"\n💥 Update failed!")

if __name__ == "__main__":
    main() 