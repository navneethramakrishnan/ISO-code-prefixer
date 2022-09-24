import pandas as pd
import os

#Change these to file paths for KX, ISO codes and output file
kx_path = '/Users/navneethramakrishnan/Desktop/ww_kx.xlsx'
iso_codes_path = '/Users/navneethramakrishnan/Desktop/iso_codes.xlsx'
output_filename = '/Users/navneethramakrishnan/Desktop/updated_kx.xlsx'

kx_list_df = pd.read_excel(open(kx_path,'rb'), sheet_name='Sheet 1')
iso_codes_df = pd.read_excel(open(iso_codes_path,'rb'), sheet_name='Sheet 1')

#Create a dictionary with country names as keys and ISO codes as values
iso_dict = {}
for i, country in enumerate(iso_codes_df.iloc[:,1]):
    iso_dict[country] = iso_codes_df.iloc[i, 0]
    
#Remove paranthesis and following part from any country's name e.g. France (including Corsica) becomes France
for i, country in enumerate(kx_list_df.iloc[:,6]):
    country_str = str(country)
    if '(' in country_str:
        index = country_str.index("(");
        country_str = country_str[0:index-1]
        kx_list_df.iloc[i,6] = country_str
    if country_str in iso_dict.keys():
        kx_list_df.iloc[i,6] = iso_dict[country_str]+':'+country_str

#Print country's ISO code in front of name e.g. France -> FR:France
for country in kx_list_df.iloc[:,6]:
    if str(country)[2]!=':':
        print(country)
        
#Output Excel file. Remember to change to xls for eHalls 
kx_list_df.to_excel(output_filename, index = False)