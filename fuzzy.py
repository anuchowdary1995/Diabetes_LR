import pandas as pd
import fuzzywuzzy
from fuzzywuzzy import fuzz
fuzz.ratio('plot18 25 MK/237 Asquith Avenue Melksham SN12 7GY UK A15101741533', 'plot77 24 MK/237 Gladstone Road Melksham SN12 7GZ UK A15101741598')
fuzz.token_sort_ratio('plot18 25 MK/237 Asquith Avenue Melksham SN12 7GY UK A15101741533', 'plot77 24 MK/237 Gladstone Road Melksham SN12 7GZ UK A15101741598')
fuzz.token_set_ratio('plot18 25 MK/237 Asquith Avenue Melksham SN12 7GY UK A15101741533', 'plot77 24 MK/237 Gladstone Road Melksham SN12 7GZ UK A15101741598')
new_data=pd.read_excel('C:/Users/Anusha/Downloads/just.xlsx')
new_data_col=(new_data.columns).tolist()
#print(new_data_col)
new_data["Final_String_new"]=""
#print(new_data)
for i in new_data_col:
    new_data["Final_String_new"]=new_data["Final_String_new"]+" "+new_data[i].astype(str)
print(new_data["Final_String_new"][0])
master_data=pd.read_excel("C:/Users/Anusha/Downloads/just1.xlsx")
master_data_col=master_data.columns.tolist()
master_data["Final_String_exist"]=""
for i in master_data_col:
    master_data["Final_String_exist"]=master_data["Final_String_exist"]+" "+master_data[i].astype(str)

print(master_data["Final_String_exist"][0])
new_data["NAD Key"]=""
output=pd.DataFrame()
output["Final_String_new"]=new_data["Final_String_new"]
output["Final_String_exist"]=""
output["NAD Key"]=""
for i in range(0,len(output)):
    for j in range(0,len(master_data)):        
        f_ratio=fuzz.ratio(output["Final_String_new"][i],master_data["Final_String_exist"][j])
        print(f_ratio)
        
        if f_ratio > 75:
            output.loc[output.index[i],"Final_String_exist"]=master_data["Final_String_exist"][j]

            output.loc[output.index[i],"NAD Key"]=master_data["NAD Key"][j]
        
print(output)
output.to_csv("C:/Users/Raja/Downloads/just3.csv")
