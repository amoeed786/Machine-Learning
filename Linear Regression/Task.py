import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

dataset=pd.read_csv('train_for_Pre.csv')
traindataset=pd.read_csv('test_for_Pre.csv')
numeric_columns = dataset.select_dtypes(include=['float', 'int']).columns
dataset[numeric_columns] = dataset[numeric_columns].fillna(dataset[numeric_columns].mean(axis=0))
X_train=dataset.iloc[:,0]
y_train=dataset.iloc[:,1]
X_test=traindataset.iloc[:,0]
y_test=traindataset.iloc[:,1]
model=LinearRegression()
model.fit(np.array(X_train).reshape(-1,1),np.array(y_train))
y_pred=model.predict(np.array(X_test).reshape(-1,1))
mse=mean_squared_error(np.array(y_test),np.array(y_pred))
print(f'Mean Square Error: {mse}')
plt.scatter(X_test, y_test, color='black', label='Actual Data')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regression Line')
plt.xlabel('x')
plt.ylabel('log(x)')
plt.title('Linear Regression Example')
plt.legend()
plt.show()
