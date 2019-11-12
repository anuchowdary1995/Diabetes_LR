import pandas as pd
import numpy as np
import fuzzywuzzy as fw
#import fuzzy
data1=pd.read_excel('C:/Users/Anusha/Downloads/just.xlsx')
data2=pd.read_excel('C:/Users/Anusha/Downloads/just1.xlsx')
print (data1)
print("....................................")
print(data2)

x = data1.to_string(header=False,
                  index=False,
                  index_names=False).split('\n')
print(x)

vals = [' '.join(i.split()) for i in x]
print(vals)

df = pd.DataFrame({'new':vals})
print (df)

x = data1.to_string(header=False,
                  index=False,
                  index_names=False).split('\n')
als = [' '.join(i.split()) for i in x]
df = pd.DataFrame({'new':vals})
print (df)


datakey=data2.drop(["NAD Key"],axis=1)
#print(datakey)
data_col=(datakey.columns).tolist()
#print(data_col)

datakey["Final_String_new"]=""
for i in data_col:
    datakey["Final_String_new"]=datakey["Final_String_new"]+" "+datakey[i].astype(str)
#print(data2)

print(df)
print(datakey["Final_String_new"])


from fuzzywuzzy import fuzz
for i in range(0,len(df)):
    for j in range(0,len(datakey)):
        f_ratio=fuzz.ratio(df["new"][i],datakey["Final_String_new"][j])
        print(f_ratio)
        
        if f_ratio > 50:
            output.loc[output.index[i],"Final_String_exist"]=master_data["Final_String_exist"][j]

            output.loc[output.index[i],"NAD Key"]=master_data["NAD Key"][j]
