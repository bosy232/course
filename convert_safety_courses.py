import pandas as pd
import json
import hashlib
import re

def clean_text(text):
    """Clean and normalize text data"""
    if pd.isna(text):
        return ""
    
    # Convert to string and strip whitespace
    text = str(text).strip()
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text

def generate_code(name, department, course_name):
    """Generate a unique code based on name, department, and course"""
    # Combine name, department, and course name
    combined = f"{name}_{department}_{course_name}"
    
    # Create hash
    hash_object = hashlib.md5(combined.encode())
    hash_hex = hash_object.hexdigest()
    
    # Take first 8 characters for a shorter code
    return hash_hex[:8].upper()

def convert_excel_to_json():
    """Convert Safety courses Excel file to JSON"""
    
    try:
        # Read the Excel file
        print("Reading Safety courses Excel file...")
        df = pd.read_excel('Safety courses 2025 Jan to june 2025.xlsx')
        
        print(f"Excel file loaded successfully!")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        
        # Clean the data
        print("\nCleaning data...")
        
        # Convert all columns to string and clean them
        for column in df.columns:
            df[column] = df[column].apply(clean_text)
        
        # Remove rows where all values are empty
        df = df.dropna(how='all')
        
        print(f"Data cleaned! Remaining rows: {len(df)}")
        
        # Convert DataFrame to list of dictionaries
        records = []
        
        for index, row in df.iterrows():
            # Skip if the first column (usually name) is empty
            if not row.iloc[0]:
                continue
                
            record = {}
            
            # Add all columns to the record
            for column in df.columns:
                record[column] = row[column]
            
            # Generate a unique code
            name = row.iloc[0] if len(row) > 0 else ""
            department = row.iloc[2] if len(row) > 2 else ""
            course_name = row.iloc[1] if len(row) > 1 else ""
            
            record['code'] = generate_code(name, department, course_name)
            
            records.append(record)
        
        print(f"Processed {len(records)} records")
        
        # Save to JSON file
        output_file = 'Safety courses.json'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Successfully converted Excel to JSON!")
        print(f"Output file: {output_file}")
        print(f"Total records: {len(records)}")
        
        # Show sample of the data
        if records:
            print(f"\nSample record:")
            print(json.dumps(records[0], ensure_ascii=False, indent=2))
        
        return True
        
    except FileNotFoundError:
        print("❌ Error: Excel file 'Safety courses 2025 Jan to june 2025.xlsx' not found!")
        return False
    except Exception as e:
        print(f"❌ Error converting Excel to JSON: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Starting Safety courses Excel to JSON conversion...")
    print("=" * 50)
    
    success = convert_excel_to_json()
    
    if success:
        print("\n" + "=" * 50)
        print("🎉 Conversion completed successfully!")
    else:
        print("\n" + "=" * 50)
        print("💥 Conversion failed!") 