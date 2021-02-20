import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

outliers = []

def detect_outlier(data):
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    for y in data:
        zScore = (y - mean) / std
        if np.abs(zScore) > threshold:
            outliers.append(y)
    return outliers

train = pd.read_csv('train.csv')
train.SalePrice.describe()

size = train.shape[0]  # Gives number of rows


#Next, we'll check for skewness
print ("Skew is:", train.SalePrice.skew())
plt.hist(train.SalePrice, color='blue')
plt.show()

#Working with Numeric Features
numeric_features = train.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['SalePrice'].sort_values(ascending=False)[:5], '\n')
print (corr['SalePrice'].sort_values(ascending=False)[-5:])
quality_pivot = train.pivot_table(index='OverallQual',
                                  values='SalePrice', aggfunc=np.median)
print(quality_pivot)
#Notice that the median sales price strictly increases as Overall Quality increases.
quality_pivot.plot(kind='bar', color='blue')
plt.xlabel('Overall Quality')
plt.ylabel('Median Sale Price')
plt.xticks(rotation=0)
plt.show()

##Null values
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

##handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))

## scatter plot of Sale Price and Garage Area
plt.scatter(train['SalePrice'], train['GarageArea'])
plt.show()

z = np.abs(stats.zscore(data))

dataset_cleared_zscore = train[(z < 3).all(axis=1)]
dataset_cleared_zscore
dataset_cleared_zscore.shape #it will remove some rows
train.shape #actual rows

plt.scatter(dataset_cleared_zscore['SalePrice'], dataset_cleared_zscore['GarageArea'])
plt.show()