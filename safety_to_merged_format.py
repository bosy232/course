import pandas as pd
import json
import numpy as np
import hashlib
from datetime import datetime

def convert_safety_to_merged_format(excel_file, output_file="Safety courses.json"):
    """Convert Safety courses Excel directly to merged_employees.json format"""
    
    print(f"🚀 Converting {excel_file} to {output_file} (merged format)")
    print("=" * 60)
    
    try:
        # Read Excel file
        print("📖 Reading Excel file...")
        df = pd.read_excel(excel_file, header=None)
        
        print(f"📊 Original shape: {df.shape}")
        
        # Based on the examination, we know the header is in row 2 (index 2)
        header_row = 2
        print(f"📋 Using row {header_row} as header (index 2)")
        
        # Set column names from header row
        df.columns = df.iloc[header_row]
        
        # Remove rows before header and reset index
        df = df[header_row + 1:].reset_index(drop=True)
        
        # Remove columns with NaN names
        df = df.loc[:, ~df.columns.isna()]
        
        # Remove columns where all values are NaN
        df = df.dropna(axis=1, how='all')
        
        # Replace NaN values with empty strings
        df = df.replace({np.nan: ""})
        
        print(f"🧹 Cleaned shape: {df.shape}")
        print(f"📋 Column names: {list(df.columns)}")
        
        # Group by employee (Participant Name)
        employees = {}
        
        for index, row in df.iterrows():
            name = row.get("Participant Name ", "").strip()
            if not name:
                continue
            
            # Generate employee code based on name
            employee_code = hashlib.sha256(name.encode()).hexdigest()[:8]
            
            if name not in employees:
                employees[name] = {
                    "name": name,
                    "code": employee_code,
                    "department": row.get("Department", ""),
                    "courses": []
                }
            
            # Add course to employee
            course_data = {
                "course_name": row.get("Course Name", ""),
                "date_of_course": row.get("Date of Course", ""),
                "date_of_expiry": row.get("Date of Expiry", ""),
                "department": row.get("Department", "")
            }
            
            # Convert datetime objects to string format
            if isinstance(course_data["date_of_course"], datetime):
                course_data["date_of_course"] = course_data["date_of_course"].strftime("%d %b %Y")
            if isinstance(course_data["date_of_expiry"], datetime):
                course_data["date_of_expiry"] = course_data["date_of_expiry"].strftime("%d %b %Y")
            
            employees[name]["courses"].append(course_data)
        
        # Convert to list
        merged_list = list(employees.values())
        
        # Save to JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(merged_list, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Successfully converted to {output_file}")
        print(f"📊 Total employees: {len(merged_list)}")
        print(f"📋 Total courses: {sum(len(emp['courses']) for emp in merged_list)}")
        
        # Show sample data
        if merged_list:
            print(f"\n📋 Sample employee:")
            print(json.dumps(merged_list[0], ensure_ascii=False, indent=2))
        
        # Show statistics
        print(f"\n📈 Statistics:")
        unique_courses = set()
        for emp in merged_list:
            for course in emp['courses']:
                unique_courses.add(course['course_name'])
        
        print(f"   - Unique courses: {len(unique_courses)}")
        print(f"   - Courses: {list(unique_courses)}")
        
        return output_file
        
    except Exception as e:
        print(f"❌ Error converting file: {str(e)}")
        return None

def main():
    """Main function"""
    excel_file = "Safety courses 2025 Jan to june 2025.xlsx"
    
    # Convert Excel directly to merged format
    output_file = convert_safety_to_merged_format(excel_file)
    
    if output_file:
        print(f"\n🎉 Conversion completed successfully!")
        print(f"📁 Output file: {output_file}")
        print(f"✅ File is now in the same format as merged_employees.json")
    else:
        print(f"\n💥 Conversion failed!")

if __name__ == "__main__":
    main() 