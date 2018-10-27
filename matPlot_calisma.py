import pandas as pd 
import matplotlib.pyplot as plt 

df= pd.read_csv("iris.csv")
"""
print(df.columns)
#print(df.Species)
print(df.Species.unique()) # Sadece kaç tür varsa onları yazdırır

print(df.info())
print(df.describe())
setosa = df[df.Species == "Iris-setosa"]
versiColor  = df[df.Species == "Iris-versicolor"]
print(len(setosa.Id) )
print(len(versiColor.Id))
"""
df1 = df.drop(["Id"],axis=1)
df1.plot()
plt.show()