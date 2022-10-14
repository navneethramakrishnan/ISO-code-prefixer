# ISO-code-prefixer 
Adds a country's ISO code prefix to eHalls KX lists. Also deletes unncessary columns from the format given.

## Usage
Step 1: Download and store the file `iso_codes.xlsx` on your machine. Download the input KX file from College in the same location  
Step 2: Change the paths in `ISO_country_codes.py` to the paths where the files in Step 1 were stored  
Step 3: Check that the input KX file has columns with column names matching those in ehalls_list_of_cols  
Step 4: Check that the sheet name of the input KX file is in the format 'Woodward_MMM_YYYY'  
Step 5: Run `ISO_country_codes.py`  
Step 6: Open the newly created file stored under `output_filename` and save it as .xls instead of .xlsx.  
Step 7: Upload to eHalls  
