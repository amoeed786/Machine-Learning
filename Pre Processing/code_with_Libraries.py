import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df1=pd.read_csv('Data.csv')
numeric_columns = df1.select_dtypes(include=['float', 'int']).columns
df1[numeric_columns] = df1[numeric_columns].fillna(df1[numeric_columns].mean(axis=0))
string_columns =df1.select_dtypes(include=[object]).columns
df1[string_columns] = df1[string_columns].fillna(df1[string_columns].mode().iloc[0])
continuous_features = ['Age','Salary']
scaler = StandardScaler()
df1[continuous_features] = scaler.fit_transform(df1[continuous_features])
columns_to_one_hot_encode = ['Country','Purchased']
df1=pd.get_dummies(df1, columns=columns_to_one_hot_encode)
df1.drop_duplicates(inplace=True)
df1.to_csv('newdata.csv',index=False)
x=df1.iloc[:,:-2]
y=df1.iloc[:,-2:]
X_train, X_test, y_train, y_test = train_test_split(x,y , test_size=0.2, random_state=42)