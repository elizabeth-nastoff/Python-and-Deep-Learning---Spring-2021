import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# added to transform non-numeric data
from sklearn.preprocessing import LabelEncoder
encode = LabelEncoder()

data = pd.read_csv("Restaurant Revenue.csv")

# drops missing values
data = data.select_dtypes(include=[np.number]).interpolate().dropna()

# drop revenue outliers
#print(data['revenue'].describe())
outlier = np.where(data['revenue'] > 10000000)
data.drop(outlier[0],inplace=True)

X = data[['P28', 'P26', 'P29', 'P11', 'P9']]
y = np.log(data['revenue'])
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=118, test_size=.30)

reg = linear_model.LinearRegression()
model = reg.fit(X_train, y_train)

print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)

#RMSE Score
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

#scatter plot of predicted to actual
actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75, color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted revenue')
plt.ylabel('Actual revenue')
plt.title('Linear Regression Model')
plt.show()