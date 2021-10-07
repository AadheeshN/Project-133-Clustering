# Import Modules
import pandas as pd
import plotly.express as px
import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = []
with open("final_data.csv", 'r') as f:
  csvreader = csv.reader(f)
  for data in csvreader:
    data.append(data)

headers = data[0]
star_data = data[1:]

radius = []
mass = []

for star_data in star_data:
    mass.append(star_data[3])
    radius.append(star_data[4])

x = []
for index, mass in enumerate(mass):
  temp_list = [radius[index], mass]
  x.append(temp_list)

WCSS = []
for i in range(1,11):
  k_means = KMeans(n_clusters = i, init ='k-means++', random_state = 42)
  k_means.fit(x)
  WCSS.append(k_means.inertia_)

plt.figure(figsize = (10,5))
sns.lineplot(range(1,11), WCSS, marker = 'o', color = 'green')
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()