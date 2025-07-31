import pandas as pd
import json
import numpy as np
import hashlib
import os

def examine_excel_structure(excel_file):
    """Examine the structure of Excel file"""
    print(f"🔍 Examining Excel file: {excel_file}")
    print("=" * 60)
    
    try:
        # Read Excel file without header first
        df = pd.read_excel(excel_file, header=None)
        
        print(f"📊 File shape: {df.shape}")
        print(f"📋 First 10 rows:")
        print(df.head(10))
        print("\n" + "=" * 60)
        
        # Check for potential header rows
        print("🔍 Looking for header row...")
        for i in range(min(10, len(df))):
            non_empty = df.iloc[i].notna().sum()
            print(f"Row {i}: {non_empty} non-empty cells")
            if non_empty > len(df.columns) * 0.3:  # More than 30% have data
                print(f"  -> Potential header row!")
                print(f"  -> Values: {list(df.iloc[i])}")
        
        return df
        
    except Exception as e:
        print(f"❌ Error examining file: {str(e)}")
        return None

def convert_safety_to_json(excel_file, output_file="Safety courses.json"):
    """Convert Safety courses Excel to JSON like courses.xlsx"""
    
    print(f"\n🚀 Converting {excel_file} to {output_file}")
    print("=" * 60)
    
    try:
        # Read Excel file
        print("📖 Reading Excel file...")
        df = pd.read_excel(excel_file, header=None)
        
        print(f"📊 Original shape: {df.shape}")
        
        # Find header row (usually row 2 or 3)
        header_row = None
        for i in range(min(5, len(df))):
            if df.iloc[i].notna().sum() > len(df.columns) * 0.5:
                header_row = i
                break
        
        if header_row is None:
            header_row = 0
        
        print(f"📋 Using row {header_row} as header")
        print(f"📋 Header values: {list(df.iloc[header_row])}")
        
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
        
        # Generate unique codes for each row
        def generate_code(row, idx):
            # Try to use name column if available
            name_cols = [col for col in df.columns if 'name' in col.lower() or 'participant' in col.lower()]
            if name_cols:
                name = str(row.get(name_cols[0], f"row_{idx}"))
            else:
                name = f"row_{idx}"
            base = f"{name}-{idx}"
            return hashlib.sha256(base.encode()).hexdigest()[:8]
        
        df['code'] = [generate_code(row, idx) for idx, row in df.iterrows()]
        
        # Convert to dictionary format
        data = df.to_dict(orient='records')
        
        # Save to JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Successfully converted to {output_file}")
        print(f"📊 Total records: {len(data)}")
        
        # Show sample data
        if data:
            print(f"\n📋 Sample record:")
            print(json.dumps(data[0], ensure_ascii=False, indent=2))
        
        return output_file
        
    except Exception as e:
        print(f"❌ Error converting file: {str(e)}")
        return None

def main():
    """Main function"""
    excel_file = "Safety courses 2025 Jan to june 2025.xlsx"
    
    # First examine the file structure
    df = examine_excel_structure(excel_file)
    
    if df is not None:
        # Then convert to JSON
        output_file = convert_safety_to_json(excel_file)
        
        if output_file:
            print(f"\n🎉 Conversion completed successfully!")
            print(f"📁 Output file: {output_file}")
        else:
            print(f"\n💥 Conversion failed!")
    else:
        print(f"\n💥 Could not examine file!")

if __name__ == "__main__":
    main() 