import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn import preprocessing


data = pd.read_csv("CC.csv")

#print(data.isna().sum().sum())
# originally 314 null values

# replaces null values with the column mean
data.fillna(data.mean(), inplace=True)

#print(data.isna().sum().sum())
# now shows 0 null values

# take all columns except for ID
data.drop("CUST_ID", axis=1, inplace=True)
y = data['TENURE']

x = data.drop("TENURE", axis=1)

# elbow method to know the number of clusters
wcss = []
for i in range(1,30):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,30),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

# chose k based off elbow method
nclusters = 6
km = KMeans(n_clusters=nclusters)
km.fit(x)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(x)

# silhouette score
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)
