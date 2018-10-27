import pandas as pd
import numpy as np 
dictionary={"NAME":["ali","veli","kenan","hilal","ayse","evren"],
            "AGE":[15,16,17,33,45,66],
            "MAAS":[100,150,240,350,110,220]}

dataFrame1 =pd.DataFrame(dictionary)
"""
print(dataFrame1)
print("**********************")
head =dataFrame1.head()
print(head)
print("**********************")
tail = dataFrame1.tail()
print(tail)
print("**********************")
head =dataFrame1.head(6)
print(head)
print("**********************")
print(dataFrame1.columns)
print("**********************")
print(dataFrame1.info())
print("**********************")
print(dataFrame1.dtypes)
print("**********************")
print(dataFrame1.describe()) #Sadece Numeric features ile ilgilenir ( Columns age ve maas)
print("**********************")

print(dataFrame1["NAME"])
print(dataFrame1["AGE"])
print(dataFrame1.AGE)
print("*******")

dataFrame1["new feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1)
print(dataFrame1.new_feature)
print(dataFrame1.loc[:,"AGE"])
print(dataFrame1.loc[:3,"AGE"])#0 dan 3 e satır seç, Age sutünündan.
print(dataFrame1.loc[:3,["AGE","NAME"]])
print(dataFrame1.loc[::-1,:]) #tersten yazdır.
print(dataFrame1.loc[:,"NAME"])
print(dataFrame1.iloc[:,1])

filtre1 = dataFrame1.MAAS > 200
print(filtre1)
print(type(filtre1))
filtrelenmis_data = dataFrame1[filtre1]
print(filtrelenmis_data)
filtre2 =dataFrame1.AGE <20
filtrelenmis_data = dataFrame1[filtre1 & filtre2]
print(filtrelenmis_data)

print(dataFrame1[dataFrame1.AGE>60])

print(dataFrame1.MAAS.mean()) #pandas kullanılarak ortalama bulma
#print(np.mean(dataFrame1.MAAS)) #Numpy kullanarak ortalama bulma
ortalama_maas = dataFrame1.MAAS.mean()
dataFrame1["maas_seviyesi"]= ["dusuk" if ortalama_maas > each  else "yuksek" for each in dataFrame1.MAAS]
print(dataFrame1)
#for each in dataFrame1.MAAS:
#   if(ortalama_maas>each):
#      print("dusuk")
# else:
#    print("yuksek")

#dataFrame1.columns = [each.lower()  for each in dataFrame1.columns]
#print(dataFrame1.columns)

dataFrame1.columns =[each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns] 
#sütün isimlerinde boşlukları kaldırığ yerine _ koyuyor
# dataFrame1.columns = [each.replace(" ","_") if (len(each.split()) > 1) else each for each in dataFrame1.columns]
#Bu da başka bir kullanım.
print(dataFrame1.columns)

dataFrame1.drop(["new_feature"],axis=1,inplace=True)
#dataFrame1 = dataFrame1.drop(["new_feature"],axis=1)
print(dataFrame1)

data1 =dataFrame1.head()
data2  = dataFrame1.tail()

data_concat = pd.concat([data1,data2],axis=0)
print("*********")
print(data_concat)

maas = dataFrame1.MAAS
age =dataFrame1.AGE
data_h_concat = pd.concat([maas,age],axis=1)
print(data_h_concat)
"""

dataFrame1["list_comp"] = [each*2 for each in dataFrame1.AGE]
print(dataFrame1)

def multiply(age):
    return age*2

dataFrame1["apply_metodu"]=dataFrame1.AGE.apply(multiply) #BU ÖNEMLİ BENCE
print(dataFrame1)