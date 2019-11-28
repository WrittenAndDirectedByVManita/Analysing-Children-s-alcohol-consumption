#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:46:18 2018

@author: Manita
"""


#******************************************************************************
# Correlation
#******************************************************************************

table = agg.corr()

mask = np.zeros_like(table)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    plt.figure(figsize = (10,5))
    sns.heatmap(table, 
            xticklabels=table.columns.values,
            yticklabels=table.columns.values,
            linewidths=0.1, annot= True,mask=mask,square=False)

plt.show()

# Tirar: friends_help e first_drunk

agg.drop(columns = ["friends_help","first_drunk"],inplace=True)
# agg.reset_index(inplace=True)
#******************************************************************************
# PCA
#******************************************************************************


# Normalize
to_clust = agg.copy().drop(columns=["country",'CODE'])

my_scaler = StandardScaler()

to_clust = my_scaler.fit_transform(to_clust)

to_clust = pd.DataFrame(to_clust, columns = agg.drop(columns=["country",'CODE']).columns)

n_components = 12

pca = PCA(n_components= n_components)

principalComponents = pca.fit_transform(to_clust)

# Explained variance by each component

pca_board = pd.DataFrame({"Explained_Var":np.round(pca.explained_variance_ratio_*100,decimals=1),
                          "Cumulative_Var":np.round(np.cumsum(pca.explained_variance_ratio_*100),decimals= 2)})
pca_board.index.name = 'PC'
pca_board.index += 1 

print (pca_board)

#elbow graph
plt.figure(figsize=(10,7))
plt.plot(pca_board.Explained_Var, color = "black", label = "explained variance")
plt.xlabel('number of components')
plt.ylabel('explained variance')
plt.title ("Principal components elbow graph", loc = "left",fontweight = "bold")
plt.axvline(x = 7, alpha = 0.4, color = "salmon", linestyle = "--", label = "cumulative explained var > 80%")
plt.legend()
plt.show()

#print(np.round(pca.explained_variance_,decimals=1))

'''7 components'''

# Revert PCA effect
# pca.inverse_transform(principalComponents)

pca_index= []

for i in range(1,n_components+1):
    pca_index.append('PC'+str(i))
    
print (pd.DataFrame(pca.components_,
                    columns=to_clust.columns,
                    index = pca_index))


agg_pca = pd.DataFrame(principalComponents,
                     columns = pca_index)



# PCA is not a good option

#******************************************************************************
# K means
#******************************************************************************

# agg_filtered = agg[~agg['country'].isin(["Greenland","Macedonia"])]
# to_clust = agg_filtered.copy().drop(columns = "country")

to_clust = agg.copy().drop(columns=["country",'CODE'])
my_scaler = StandardScaler()
to_clust = my_scaler.fit_transform(to_clust)
to_clust = pd.DataFrame(to_clust, columns = agg.drop(columns=["country",'CODE']).columns)

# elbow
cluster_range = range(1,7)
cluster_errors = []
sse = {}
for k in cluster_range:
    kmeans = KMeans(n_clusters=k, 
                random_state=0,
                n_init = 10,
                max_iter = 300).fit(to_clust)
    to_clust["clusters"] = kmeans.labels_
    #print(data["clusters"])
    sse[k] = kmeans.inertia_
    cluster_errors.append(kmeans.inertia_)
    # Inertia: Sum of distances of samples to their closest cluster center
plt.figure(figsize=(8,5))
plt.plot(list(sse.keys()), list(sse.values()),
         linewidth=1.5,
         linestyle="-",
         marker = "X",
         markeredgecolor="salmon",
         color = "black")
plt.title ("K-Means elbow graph", loc = "left",fontweight = "bold")
plt.xlabel("Number of cluster")
plt.ylabel("SSE")
plt.axvline(x = 6, alpha = 0.4, color = "salmon", linestyle = "--")
plt.show()

clusters_df = pd.DataFrame({"cluster_errors":cluster_errors})
clusters_df.index += 1
clusters_df.index.name = "num_clusters"
print (clusters_df)

# Final number of clusters: 6 or 7

kmeans_ine=kmeans.inertia_

'''
# Check the clusters
agg_clusters = pd.DataFrame(kmeans.cluster_centers_,columns=to_clust.columns)
print (agg_clusters)
'''

# Cluster frequency

freq = to_clust 
print("\nAbsolute frequency of each cluster:\n")
print(freq["clusters"].value_counts())
print("\nRelative frequency of each cluster:\n")
print(np.round(freq["clusters"].value_counts()/
               len(freq)*100,
               decimals=2))
plt.subplots(figsize=(7, 3))
plt.title ("Cluster frequency", loc = "left",fontweight = "bold")
sns.countplot(x=freq["clusters"], data=freq, color="skyblue", edgecolor = "black")
sns.despine(left='False') 
plt.ylabel("") 
plt.show()

# means
agg_clustered = agg.copy()
agg_clustered['clusters'] = to_clust.clusters

agg_clusters = agg_clustered.groupby(['clusters']).mean()
print(agg_clusters)

# Visualize
# these clusters are not good to visualize in a 2D plot, a map is needed

table = agg_clustered

x = table['alcopops']
y = table['drink_day']
c = table['clusters']

plt.scatter(x, y, c=c)
plt.show()


#******************************************************************************
#Hierarchical
#******************************************************************************

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage 
from scipy.cluster import hierarchy
import sklearn
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm

# Dendogram
to_clust = agg.copy().drop(columns=["country",'CODE'])
to_clust = my_scaler.fit_transform(to_clust)
to_clust = pd.DataFrame(to_clust, columns = agg.drop(columns=["country",'CODE']).columns)

Z = linkage(to_clust, method = 'ward')
plt.subplots(figsize=(8, 10))
dendrogram(Z,
           truncate_mode='lastp',
           p=20,
           orientation = 'top',
           leaf_rotation=45.,
           leaf_font_size=10.,
           show_contracted=True,
           show_leaf_counts=True)
plt.title ("Clustering Dendogram", loc = "center",fontweight = "bold")
plt.xlabel('Cluster Size')
plt.ylabel('Distance')
plt.axhline(y=7.3, color = "salmon", linestyle = "--")
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.show()

# Hierarchical clustering

to_clust = agg.copy().drop(columns=["country",'CODE'])
to_clust = my_scaler.fit_transform(to_clust)
to_clust = pd.DataFrame(to_clust, columns = agg.drop(columns=["country",'CODE']).columns)

k=6

Hclustering = AgglomerativeClustering(n_clusters=k,
                                      affinity='euclidean',
                                      linkage='ward')

# Get clusters
my_HC = Hclustering.fit(to_clust)

my_labels = pd.DataFrame(my_HC.labels_)
my_labels.columns =  ['clusters']

# agg clustered
agg_clustered = agg.copy()
agg_clustered['clusters'] = my_labels.clusters.tolist()



# Engage clusters mean

agg_h = agg_clustered.groupby(['clusters']).mean()
print(agg_h)

# Cluster frequency

freq = agg_clustered 
print("\nAbsolute frequency of each cluster:\n")
print(freq["clusters"].value_counts())
print("\nRelative frequency of each cluster:\n")
print(np.round(freq["clusters"].value_counts()/
               len(freq)*100,
               decimals=2))
plt.subplots(figsize=(7, 3))
sns.countplot(x=freq["clusters"], data=freq, palette="Oranges")
sns.despine(left='False')  
plt.show()


#******************************************************************************
# EM
#******************************************************************************

# Expectation-Maximization

to_clust = agg.copy().drop(columns=["country",'CODE'])
to_clust = my_scaler.fit_transform(to_clust)
to_clust = pd.DataFrame(to_clust, columns = agg.drop(columns=["country",'CODE']).columns)


# correr um k means para ter os pontos médios
from sklearn import mixture
gmm = mixture.GaussianMixture(n_components=6,
                              covariance_type='full',
                              init_params='kmeans',
                              max_iter=1000,
                              n_init=15)

gmm.fit(to_clust)
EM_labels_ = gmm.predict(to_clust)
#Elbow
EM_score_ = gmm.score(to_clust)
#Individual
EM_score_samp = gmm.score_samples(to_clust)
#Individual
EM_pred_prob = gmm.predict_proba(to_clust)


unique_clusters, counts_clusters = np.unique(EM_labels_, return_counts = True)
print(np.asarray((unique_clusters, counts_clusters)).T)
#Check the distribution
gmm.weights_
gmm.means_


agg_clustered = agg.copy()
agg_clustered['cluster'] = EM_labels_

# cluster means

print(agg_clustered.groupby(['cluster']).mean())




#******************************************************************************
# K means with centroids from Hierarchical
#******************************************************************************

# agg_filtered = agg[~agg['country'].isin(["Greenland","Macedonia"])]
# to_clust = agg_filtered.copy().drop(columns = "country")

init_centroids=agg_h.as_matrix()

to_clust = agg.copy().drop(columns=["country",'CODE'])
my_scaler = StandardScaler()
to_clust = my_scaler.fit_transform(to_clust)
to_clust = pd.DataFrame(to_clust, columns = agg.drop(columns=["country",'CODE']).columns)


to_clust_h=to_clust.copy()


# elbow
cluster_range = range(1,7)
cluster_errors = []
sse = {}
for k in cluster_range:
    kmeans = KMeans(n_clusters=6, 
                random_state=0,
                n_init =15,
                max_iter = 300, 
                init=init_centroids).fit(to_clust)
    to_clust_h["clusters"] = kmeans.labels_
    #print(data["clusters"])
    sse[k] = kmeans.inertia_
    cluster_errors.append(kmeans.inertia_)
    # Inertia: Sum of distances of samples to their closest cluster center
plt.figure(figsize=(8,5))
plt.plot(list(sse.keys()), list(sse.values()),
         linewidth=1.5,
         linestyle="-",
         marker = "X",
         markeredgecolor="salmon",
         color = "black")
plt.title ("K-Means elbow graph", loc = "left",fontweight = "bold")
plt.xlabel("Number of cluster")
plt.ylabel("SSE")
plt.axvline(x = 6, alpha = 0.4, color = "salmon", linestyle = "--")
plt.show()

clusters_df = pd.DataFrame({"cluster_errors":cluster_errors})
clusters_df.index += 1
clusters_df.index.name = "num_clusters"
print (clusters_df)

# Final number of clusters: 6 or 7

kh_ine=kmeans.inertia_


'''
# Check the clusters
agg_clusters = pd.DataFrame(kmeans.cluster_centers_,columns=to_clust.columns)
print (agg_clusters)
'''

# Cluster frequency

freq = to_clust_h 
print("\nAbsolute frequency of each cluster:\n")
print(freq["clusters"].value_counts())
print("\nRelative frequency of each cluster:\n")
print(np.round(freq["clusters"].value_counts()/
               len(freq)*100,
               decimals=2))
plt.subplots(figsize=(7, 3))
plt.title ("Cluster frequency", loc = "left",fontweight = "bold")
sns.countplot(x=freq["clusters"], data=freq, color="skyblue", edgecolor = "black")
sns.despine(left='False') 
plt.ylabel("") 
plt.show()

# means
agg_clustered = agg.copy()
agg_clustered['clusters'] = to_clust_h.clusters

agg_clusters_kh = agg_clustered.groupby(['clusters']).mean()
print(agg_clusters_kh)

# Visualize

table = agg_clustered

x = table['alcopops']
y = table['drink_day']
c = table['clusters']

plt.scatter(x, y, c=c)
plt.show()












