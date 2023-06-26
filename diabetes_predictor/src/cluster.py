import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/jvpalhares/datasci4health_diabetes/dev_palhares/output_cluster.csv')

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

# Get the cluster centers
centroids = kmeans.cluster_centers_

# Plot the clusters in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, -1], c=kmeans.labels_.astype(float))
ax.scatter(centroids[:, 1], centroids[:, 2], centroids[:, -1], marker='*', s=300, c='r')

# Set the axis labels
ax.set_xlabel(df.columns[1])
ax.set_ylabel(df.columns[2])
ax.set_zlabel(df.columns[-1])

plt.show()
