import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

file = open("breastcancer.csv", "r")
dataset = pd.read_csv(file, index_col='id', sep=',')
file.close()
dia = {'M':1, 'B':2}
dataset.diagnosis = [dia[item] for item in dataset.diagnosis]

norm = sc.fit_transform(dataset.iloc[:,1:31])

print(dataset)
X_train, X_test, Y_train, Y_test = train_test_split(norm, dataset.iloc[:,0],
                                                    test_size=0.25, random_state=87)

np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
