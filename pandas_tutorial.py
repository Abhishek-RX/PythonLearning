#Pandas 
#Pandas is an open-source, BSD-licensed Python library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
#Pandas is built on top of NumPy and is intended to integrate well within a scientific computing environment with many other 3rd party libraries.
#Pandas is a game-changer for data analysis in Python.  
#It provides two data structures: Series and DataFrame.
#Series: A one-dimensional labeled array capable of holding any data type.
#DataFrame: A two-dimensional labeled data structure with columns of potentially different types.
#Pandas is well suited for many different kinds of data:
#Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet
#Ordered and unordered (not necessarily fixed-frequency) time series data.
#Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels
#Any other form of observational / statistical data sets. The data actually need not be labeled at all to be placed into a pandas data structure
#Pandas provides a robust set of tools for reading and writing data between in-memory data structures and different file formats.
#Pandas can handle missing data gracefully using a custom object, NaN, to represent missing values.
#Pandas is fast. Many of the low-level algorithmic bits have been extensively tweaked in Cython code.

import pandas as pd 
import numpy as np


s = pd.Series([10, 20, 30, 40])
print(s)
print("***************************************************************************")
print(s[0])
print(s.iloc[-1])
print(s**2)

print("Sum: ",s.sum())    #sum of all elements
print("Mean: ",s.mean())   #mean of all elements
print("Median: ",s.median()) #median of all elements
print("Standard Deviation: ",s.std())    #standard deviation of all elements
print("Max: ",s.max())    #maximum of all elements
print("Min: ",s.min())    #minimum of all elements
print("Count: ",s.count())   #count of all elements
print("Unique: ",s.unique())   #unique elements
print("******************************************")
print("Check for Null: ",s.isnull())   #check for null values

print("Not Null values",s[s.notnull()])   #check for not null values

print("Indexes: ", s.index)   #indexes of the series 
print("Values: ", s.values)   #values of the series

#Creating a series with custom indexes  

s = pd.Series(["Apple", "Ball", "Cat", "Dog"], index = ['a', 'b', 'c', 'd'])
print(s)

print(s.where(s.index == "a"))   #where condition is true

print(s['a'])   #accessing the element with index 'a'

key = 'a' 
if key in s.index : 
    print("Key is present : ", s[key])
    s= s.drop(key)
    
else:
    print("Key is not present")
    
print(s)

print(s.iloc[2])  #accessing the element by default index 

print(s.loc['b'])  #accessing the element by custom made index

#creating a series with a null value 

S_Null = pd.Series([10,20,50,60,np.nan,50])
print(S_Null)

print(S_Null.isnull())   #check for null values 

S_Null = S_Null.drop(S_Null.index[S_Null.isnull()])
print(S_Null)
for value in S_Null: 
    if pd.isnull(value):
        print("Null value found")
        S_Null = S_Null.drop(S_Null.index[S_Null.isnull()])
    
print(S_Null)