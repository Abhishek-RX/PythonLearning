# 1 Year chart of nifty 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#%matplotlib inline 


data = pd.read_csv('Nifty1.csv')
print(data.shape)

print(data.head())
print(type(data))
#print(data.dtypes)
#print(data.columns)
#print(data['Date '])
data['Date '] = pd.to_datetime(data['Date '], format = '%d-%b-%Y')
plt.figure(figsize = (13,7), facecolor = "grey")                            # window size
plt.plot( data['Date '], data['Close '], label = "NIfty chart", marker =".",markersize=8, linestyle = "-")
plt.xlabel("Date", color = "White")
plt.ylabel("Price", color = "White")
plt.title("Nifty Chart" , color = "White")
plt.grid()
ax = plt.gca()
ax.set_facecolor("black")
plt.show()


