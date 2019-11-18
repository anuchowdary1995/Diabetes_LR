import pandas as pd
import fuzzywuzzy
from fuzzywuzzy import fuzz
import numpy as np
#fuzz.ratio('plot18 25 MK/237 Asquith Avenue Melksham SN12 7GY UK A15101741533', 'plot77 24 MK/237 Gladstone Road Melksham SN12 7GZ UK A15101741598')
#fuzz.token_sort_ratio('plot18 25 MK/237 Asquith Avenue Melksham SN12 7GY UK A15101741533', 'plot77 24 MK/237 Gladstone Road Melksham SN12 7GZ UK A15101741598')
#fuzz.token_set_ratio('plot18 25 MK/237 Asquith Avenue Melksham SN12 7GY UK A15101741533', 'plot77 24 MK/237 Gladstone Road Melksham SN12 7GZ UK A15101741598')
new_data=pd.read_excel('/home/neureol/Downloads/just.xlsx')
new_data_col=(new_data.columns).tolist()
#print(new_data_col)
new_data["Final_String_new"]=""
#print(new_data)
for i in new_data_col:
    new_data["Final_String_new"]=new_data["Final_String_new"]+" "+new_data[i].astype(str)
print(new_data["Final_String_new"][0])
master_data=pd.read_excel("/home/neureol/Downloads/just1.xlsx")
master_data_col=master_data.columns.tolist()
master_data_col.remove("NAD Key")
master_data["Final_String_exist"]=""
for i in master_data_col:
    master_data["Final_String_exist"]=master_data["Final_String_exist"]+" "+master_data[i].astype(str)

print(master_data["Final_String_exist"][0])
new_data["NAD Key"]=""
#output=pd.DataFrame()
#new_data["Final_String_new"]=new_data["Final_String_new"]
new_data["Final_String_exist"]=""
new_data["NAD Key"]=np.NaN
new_data["F_Ratio"]=np.NaN
new_data["Indices"]=np.NaN
output=pd.DataFrame()
output=new_data
count=1
for i in range(0,len(new_data)):
    for j in range(0,len(master_data)):        
        f_ratio=fuzz.ratio(new_data["Final_String_new"][i],master_data["Final_String_exist"][j])
        print(f_ratio)
        
        
        if f_ratio > 60:     
           # new_data.loc[new_data.index[i],"Final_String_exist"]=master_data["Final_String_exist"][j]
            if new_data.loc[new_data.index[i],"NAD Key"] is np.NaN:
                new_data.loc[new_data.index[i],"F_Ratio"]=f_ratio
                new_data.loc[new_data.index[i],"NAD Key"]=master_data["NAD Key"][j]
                new_data.loc[new_data.index[i],"Final_String_exist"]=master_data["Final_String_exist"][j]
                new_data.loc[new_data.index[i],"Indices"]=i
            else:
                new_data=new_data.append({"NAD Key":master_data["NAD Key"][j],"F_Ratio":f_ratio,"Final_String_exist":master_data["Final_String_exist"][j],"Final_String_new":new_data["Final_String_new"][i],'Primise':new_data["Primise"][i], 'ThoroughFare No':new_data["ThoroughFare No"][i], 'ThoroughFare':new_data['ThoroughFare'][i], 'ThoroughFare Name':new_data['ThoroughFare Name'][i],
       'Town':new_data['Town'][i], 'Postoutcode':new_data['Postoutcode'][i], 'PostIncode':new_data['PostIncode'][i], 'Country':new_data['Country'][i],'Indices':i},ignore_index=True)
               # new_data.loc[new_data.index[len(new_data)+1],"Final_String_exist"]=master_data["Final_String_exist"][j]

            
           # else:
Non_Matched_Data=pd.DataFrame()
Non_Matched_Data=new_data[new_data['NAD Key'].isnull()] 
Matched_Data=pd.DataFrame()
Matched_Data=new_data.loc[new_data['F_Ratio'] ==100]
print(new_data.columns)
Match_Ind_lists=Matched_Data["Indices"].tolist()
output=new_data[~new_data.Indices.isin(Match_Ind_lists)]
output=output[output['NAD Key'].notnull()] 
new_data.to_csv("/home/neureol/Desktop/ops/new_data.xlsx",index=False)
Non_Matched_Data.to_csv("/home/neureol/Desktop/ops/Non_Matched_Data.xlsx",index=False)
Matched_Data.to_csv("/home/neureol/Desktop/ops/Matched_Data.xlsx",index=False)
output.to_csv("/home/neureol/Desktop/ops/output.xlsx",index=False)
