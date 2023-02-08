# ISO-code-prefixer 
This is for Hall Management at Woodward Hall, Imperial College London.  
This code takes an input KX file, adds ISO codes and makes it eHalls compatible.  

## Usage
1. Download the input KX file from College. Download the file `iso_codes.xlsx` on your machine. Update the variables 'kx_path' and 'iso_codes_path' in 'ISO_country_codes.py'.  
2. Check that the input KX file has columns with column names matching those in `ehalls_list_of_cols`. Check that the sheet name of the input KX file is in the format 'Woodward_MMM_YYYY'.  
3. Run `ISO_country_codes.py`  
4. Open the newly created file stored under `output_filename` and upload to eHalls.
