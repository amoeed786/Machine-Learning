#### Without feature scaling ###
#### Without applying One Hot Encoding ####
#### Without backward elimination ####
import pandas as pd
df = pd.read_csv("Student_Performance.csv")
df.head()
X = df.iloc[:,:5].values
y = df.iloc[:,-1].values
y
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
X[:,2] = label_encoder.fit_transform(X[:,2])
X
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)
y_pred
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)
n = len(X_test) 
p = X_test.shape[1] 
adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-Squared:", r_squared)
print("Adjusted R-Squared:", adjusted_r_squared)
