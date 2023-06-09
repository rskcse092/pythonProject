import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py
import plotly.graph_objs as go
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

# Importing the dataset
df = pd.read_csv("C:\\Users\\CSC\\PycharmProjects\\pythonProject\\Input\\Mall_Customers.csv")
print(df.head())

#Checking the size of our data
print(df.shape)

#Changing the name of some columns
df = df.rename(columns={'Annual Income (k$)': 'Annual_income', 'Spending Score (1-100)': 'Spending_score'})
print(df)

#Looking for null values
print(df.isna().sum())

#Checking datatypes
print(df.info())

#Replacing objects for numerical values
df['Gender'].replace(['Female','Male'], [0,1],inplace=True)
print(df)

#Checking values have been replaced properly
print(df.Gender)

#Density estimation of values using distplot
plt.figure(1 , figsize = (15 , 6))
feature_list = ['Age','Annual_income', "Spending_score"]
feature_listt = ['Age','Annual_income', "Spending_score"]
pos = 1
for i in feature_list:
    plt.subplot(1 , 3 , pos)
    plt.subplots_adjust(hspace = 0.5 , wspace = 0.5)
    sns.distplot(df[i], bins=20, kde = True)
    pos = pos + 1
# plt.show()

#Count and plot gender
sns.countplot(y = 'Gender', data = df, palette="husl", hue = "Gender")
print(df["Gender"].value_counts())


#Pairplot with variables we want to study
sns.pairplot(df, vars=["Age", "Annual_income", "Spending_score"],  kind ="reg", hue = "Gender", palette="husl", markers = ['o','D'])


sns.lmplot(x = "Age", y = "Annual_income", data = df, hue = "Gender")