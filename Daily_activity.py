import pandas as pd
import glob
import os

#Will need pip install pandas in command line before run from command line

path = r'source_path\*common_file_name.file_format' #the location of the files to be scanned, * is a placeholder
r_path = r'source_path\file_name_we_want.'#the location of the resulting file without the extension
if os.path.exists(r_path + 'csv'):
   os.remove(r_path + 'csv')
if os.path.exists(r_path + 'txt'):
   os.remove(r_path + 'txt')
files = glob.glob(path)
column_list = [None] * 44
for i in range(44):
    column_list[i] = str(i + 1)
df = pd.DataFrame(columns = column_list)
for name in files:
    df_n = pd.read_csv(name, names = column_list)
    df = df.append(df_n.iloc[-1], ignore_index=True)
    del df_n
df.to_csv(r_path + 'csv', index=False, header=False)
del df