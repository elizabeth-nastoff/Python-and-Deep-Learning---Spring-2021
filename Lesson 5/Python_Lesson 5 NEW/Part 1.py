# Steps
# plot GarageArea and SalePrice in Scatter plot
# check for anomalies and delete outliar data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

# Scatter plot without changing the data
plt.scatter(data.GarageArea, data.SalePrice)
plt.xlabel("Garage Area")
plt.ylabel("Sale Price")
plt.show()

# from the first scatter plot, I was able to visually judge what points are outliers
# vales are defined in "upper" and "lower"
upper = np.where(data["GarageArea"] > 1000)
lower = np.where(data["GarageArea"] < 175)

# removes outliers from the dataset
data.drop(upper[0], inplace=True)
data.drop(lower[0], inplace = True)

# prints another scatter plot to show data after the changes
plt.scatter(data["GarageArea"], data["SalePrice"])
plt.xlabel("Garage Area")
plt.ylabel("Sale Price")
plt.show()