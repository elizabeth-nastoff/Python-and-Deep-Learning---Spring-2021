import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv("Restaurant Revenue.csv")

X = data[['Id', 'City Group', 'Type']]
y = data['revenue']

X_train, X_test, y_train, y_test = train_test_split(X,y)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))