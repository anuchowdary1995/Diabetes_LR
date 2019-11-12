import pandas as pd
import numpy as np
import fuzzywuzzy as fw
#import fuzzy

data1=pd.read_excel('C:/Users/Anusha/Downloads/just.xlsx')
data2=pd.read_excel('C:/Users/Anusha/Downloads/just1.xlsx')
print (data1)
print("....................................")
print(data2)


data_col1=(data1.columns).tolist()
data1["Final_String_new"]=" "
for i in data_col1:
    data1["Final_String_new"]=data1["Final_String_new"]+" "+data1[i].astype(str)
print(data1.Final_String_new[0])


data_col2=(data2.columns).tolist()
print(data_col2)
(data_col2).pop(8)
#print(data_col)
data2["Final_String_new"]=" "
for i in data_col2:
    data2["Final_String_new"]=data2["Final_String_new"]+" "+data2[i].astype(str)
print(data2["Final_String_new"][1])


from fuzzywuzzy import fuzz
for i in range(0,len(data1)):
    for j in range(0,len(data2)):
        f_ratio=fuzz.ratio(data1["Final_String_new"][i],data2["Final_String_new"][j])
        print(f_ratio)
        
        if f_ratio > 50:
            output.loc[output.index[i],"Final_String_exist"]=master_data["Final_String_exist"][j]

            output.loc[output.index[i],"NAD Key"]=master_data["NAD Key"][j]
    
