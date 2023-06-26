import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv('output_cluster.csv')

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

# Get the cluster centers
centroids = kmeans.cluster_centers_

# Define colors for the scatter plot based on the last column values
colors = df.iloc[:, -2]

# Plot the clusters in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, -1], c=colors, cmap='coolwarm')
ax.scatter(centroids[:, 1], centroids[:, 2], centroids[:, -1], marker='*', s=300, c='g')

# Set the axis labels
ax.set_xlabel(df.columns[1])
ax.set_ylabel(df.columns[2])
ax.set_zlabel(df.columns[-1])

plt.show()
