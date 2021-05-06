from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

dataset = pd.read_csv("breastcancer.csv")
#dataset.info()
# We see there is a blank unnamed column
# drop id and the blank column
dataset.drop(['Unnamed: 32','id'], axis = 1 , inplace=True)

# replace M and B values in diagnosis column with 1 and 0
dataset.diagnosis.replace({"M":1,"B":0},inplace=True)

# y is diagnosis
y = dataset['diagnosis']
# x is everything else left
x = dataset.drop(['diagnosis'], axis = 1)

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.25, random_state=87)

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
