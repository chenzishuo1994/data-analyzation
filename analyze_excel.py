import pandas as pd
import uuid
import time


#用来解析excel文件，并且为每个数据生成单独的GUID
df = pd.read_excel("0902.xlsx",index_col=0)
print(df)
data1 = df.values[0]
# print(data1)
# data=df['blue']
number_of_column = 3
number_of_list = 3

#message of the GUID
version = "v1.0"
user = "czs"
domin = ["require","design","manufacture","experient"]
print("")
for i in range(0,number_of_column):
    for j in range(0,number_of_list):
        global_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        data01_guid = uuid.uuid1()
        data01_new_guid = str(data01_guid) + '-' + version + "-" + domin[1] + "-" + user + "-" + global_time
        data = df.values[j]
        print("data=%i"%data[i]," ","GUID=%s"%data01_new_guid)