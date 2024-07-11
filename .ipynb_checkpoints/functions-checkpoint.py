import pandas as pd
import os
from datetime import datetime

def build_ua_pages_dataframe(folder):
    base_path = 'data'
    full_path = os.path.join(base_path, folder)
    all_data = []

    if not os.path.exists(full_path):
        raise ValueError(f"The directory {full_path} does not exist.")

    csv_files = [f for f in os.listdir(full_path) if f.endswith('.csv')]
    
    if not csv_files:
        raise ValueError(f"No CSV files found in {full_path}")

    for filename in csv_files:
        file_path = os.path.join(full_path, filename)
        print(f"Processing file: {file_path}")
        
        # Extract date range from filename
        date_range = filename.split()[-1].replace('.csv', '')
        start_date = datetime.strptime(date_range.split('-')[0], '%Y%m%d')
        
        # Determine year and quarter
        year = start_date.year
        quarter = f"Q{(start_date.month - 1) // 3 + 1}"
        
        try:
            # Read CSV file
            df = pd.read_csv(file_path, 
                             skiprows=6,
                             nrows=12,
                             thousands=',',
                             encoding='utf-8-sig')
            
            if df.empty:
                print(f"Warning: {filename} is empty")
                continue

            # Add 'total' to the first column of the second to last row
            df.iloc[-2, 0] = 'total'

            # Remove the last row (which seems to be the unwanted row)
            df = df.iloc[:-1]

            # Add year and quarter columns
            df['Year'] = year
            df['Quarter'] = quarter
            
            # Filter out rows where the first column is 'Day Index'
            df = df[df.iloc[:, 0] != 'Day Index']

            all_data.append(df)
            print(f"Successfully processed {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
    
    if not all_data:
        raise ValueError("No data was successfully read from any CSV file")

    # Combine all DataFrames
    combined_df = pd.concat(all_data, ignore_index=True)
    
    print("Columns in the combined DataFrame:")
    print(combined_df.columns.tolist())

    # Clean up the data
    percentage_columns = ['Bounce Rate']
    for col in percentage_columns:
        if col in combined_df.columns:
            combined_df[col] = combined_df[col].str.rstrip('%').astype('float') / 100.0

    if 'Avg. Session Duration' in combined_df.columns:
        combined_df['Avg. Session Duration'] = pd.to_timedelta(combined_df['Avg. Session Duration'])

    numeric_columns = ['Users', 'New Users', 'Sessions', 'Pages / Session']
    for col in numeric_columns:
        if col in combined_df.columns:
            combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce')
    
    # Save to CSV
    output_folder = os.path.join('output', folder)
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, 'consolidated-pages.csv')
    combined_df.to_csv(output_file, index=False)
    print(f"Saved consolidated data to {output_file}")

    return combined_df