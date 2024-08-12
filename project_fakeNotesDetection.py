
# coding: utf-8

# In[2]:


import pandas as pd

data=pd.read_csv('1fXr31hcEemkYxLyQ1aU1g_50fc36ee697c4b158fe26ade3ec3bc24_Banknote-authentication-dataset-.csv')

variance=data["V1"]
skewness=data["V2"]


# In[3]:


import numpy as np
data=np.array(data)
mean_data=np.mean(data)
std_dev=np.std(data)

print("mean", mean_data)
print("standard deviation", std_dev)


# In[5]:


import matplotlib.pyplot as plt
plt.xlabel('variance')
plt.ylabel('skewness')
plt.scatter(variance,skewness, alpha=0.25)
plt.show()


# In[19]:


from sklearn.cluster import KMeans

variance_skewness=np.column_stack((variance,skewness))
km_res=KMeans(n_clusters=2).fit(variance_skewness)
clusters=km_res.cluster_centers_

plt.scatter(variance,skewness, alpha=0.25)
plt.scatter(clusters[:,0],clusters[:,1], s=200)
plt.show()


# In[21]:


from sklearn.metrics import silhouette_score

silhouette_avg = silhouette_score(variance_skewness,km_res.labels_)
print("Silhouette Score:", silhouette_avg)


# In[27]:


plt.scatter(variance_skewness[:, 0], variance_skewness[:, 1], c=km_res.labels_, cmap='viridis', alpha=0.5)
plt.scatter(km_res.cluster_centers_[:, 0], km_res.cluster_centers_[:, 1], s=200, c="red", label='Cluster Centers')
plt.title('K-Means Clustering')
plt.xlabel('Variance')
plt.ylabel('Skewness')
plt.legend()
plt.show()


# In[28]:



silhouette_avg = silhouette_score(variance_skewness, km_res.labels_)
print(f"Silhouette Score: {silhouette_avg:.2f}")

