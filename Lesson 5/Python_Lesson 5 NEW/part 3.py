import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# added to transform non-numeric data
from sklearn.preprocessing import LabelEncoder
encode = LabelEncoder()

data = pd.read_csv("Restaurant Revenue.csv")

# encoded the two non-numeric features
data['City Group'] = encode.fit_transform(data['City Group'])
data['Type'] = encode.fit_transform(data['Type'])

# drops missing values
data = data.select_dtypes(include=[np.number]).interpolate().dropna()

# drop revenue outliers
#print(data['revenue'].describe())
outlier = np.where(data['revenue'] > 10000000)
data.drop(outlier[0],inplace=True)

#print(data['revenue'].describe())


# Everything besides ID and Revenue is a predictor
X = data.drop(['Id', 'revenue'], axis = 1)
y = np.log(data['revenue'])

# output data for reference
#print(data)
#print(X)
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=118, test_size=.30)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)

imp = pd.Series(index = X_train.columns, data = np.abs(reg.coef_))
imp.sort_values().plot(kind = 'bar', figsize = (13,5));
plt.show()

#imp = reg.coef_
#for i,j in enumerate(imp):
#    print('Feature: %0d, Score: %.5f' % (i,j))
#plt.bar([x for x in range(len(imp))], imp)
#plt.show()

