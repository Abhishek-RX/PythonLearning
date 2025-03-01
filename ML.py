medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
from urllib.request import urlretrieve 

urlretrieve(medical_charges_url, 'Medical.Csv')

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
Medical_df = pd.read_csv('Medical.Csv')

print(Medical_df.head())

print(Medical_df.info())

print(Medical_df.describe())

plt.hist(Medical_df['bmi'], bins = 30 , alpha = 0.7 , edgecolor = 'black')
plt.show()


