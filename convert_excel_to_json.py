import pandas as pd
import json
import numpy as np
import hashlib
import os

def convert_excel_to_json(excel_file, output_file=None):
    """
    Convert Excel file to JSON format with proper data cleaning
    
    Args:
        excel_file (str): Path to the Excel file
        output_file (str): Output JSON file name (optional)
    """
    
    try:
        # Read the Excel file
        print(f"Reading Excel file: {excel_file}")
        df = pd.read_excel(excel_file, header=None)
        
        # Display basic info about the file
        print(f"Excel file shape: {df.shape}")
        print(f"First few rows:")
        print(df.head())
        
        # Try to find the header row (usually row 2 or 3)
        header_row = None
        for i in range(min(5, len(df))):
            if df.iloc[i].notna().sum() > len(df.columns) * 0.5:  # If more than 50% of cells have data
                header_row = i
                break
        
        if header_row is None:
            header_row = 0  # Default to first row
        
        print(f"Using row {header_row} as header")
        
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
        
        print(f"Cleaned data shape: {df.shape}")
        print(f"Column names: {list(df.columns)}")
        
        # Generate unique codes for each row if 'code' column doesn't exist
        if 'code' not in df.columns:
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
        
        # Determine output filename
        if output_file is None:
            base_name = os.path.splitext(excel_file)[0]
            output_file = f"{base_name}.json"
        
        # Save to JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Successfully converted {excel_file} to {output_file}")
        print(f"📊 Total records: {len(data)}")
        print(f"📁 Output file: {output_file}")
        
        # Show sample of converted data
        if data:
            print(f"\n📋 Sample data (first record):")
            print(json.dumps(data[0], ensure_ascii=False, indent=2))
        
        return output_file
        
    except Exception as e:
        print(f"❌ Error converting Excel file: {str(e)}")
        return None

def main():
    """Main function to convert Excel files"""
    
    # List of Excel files to convert
    excel_files = [
        "Safety courses 2025 Jan to june 2025.xlsx",
        "courses.xlsx"
    ]
    
    for excel_file in excel_files:
        if os.path.exists(excel_file):
            print(f"\n{'='*50}")
            print(f"Converting: {excel_file}")
            print(f"{'='*50}")
            
            output_file = convert_excel_to_json(excel_file)
            
            if output_file:
                print(f"✅ Conversion completed for {excel_file}")
            else:
                print(f"❌ Conversion failed for {excel_file}")
        else:
            print(f"⚠️  File not found: {excel_file}")

if __name__ == "__main__":
    main() 