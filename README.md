# ISO-code-prefixer 
Takes an input KX file from College and makes it eHalls compatible.  

## Usage
Step 1: Download the input KX file from College. Download the file `iso_codes.xlsx` on your machine. Update the variables 'kx_path' and 'iso_codes_path' in 'ISO_country_codes.py'.  
Step 2: Check that the input KX file has columns with column names matching those in `ehalls_list_of_cols`. Check that the sheet name of the input KX file is in the format 'Woodward_MMM_YYYY'.  
Step 3: Run `ISO_country_codes.py`  
Step 4: Open the newly created file stored under `output_filename` and save it as .xls instead of .xlsx.  
Step 5: Upload to eHalls  
