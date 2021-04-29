from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt

data = pd.read_csv("CC.csv")

# replaces null values with the column mean
data.fillna(data.mean(), inplace=True)

# take all columns except for ID
data.drop("CUST_ID", axis=1, inplace=True)
y = data['TENURE']


x = data.drop("TENURE", axis=1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)

# Apply transform to both the training set and the test set.
x_scaler = scaler.transform(x)
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,data[['TENURE']]],axis=1)
print(finaldf)

newX = finaldf.copy()

# elbow method to know the number of clusters
wcss = []
for i in range(1,30):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(newX)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,30),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

# chose k based off elbow method
nclusters = 6
km = KMeans(n_clusters=nclusters)
km.fit(newX)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(newX)

# silhouette score
score = metrics.silhouette_score(newX, y_cluster_kmeans)
print(score)