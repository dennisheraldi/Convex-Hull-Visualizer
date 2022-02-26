import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from myConvexHull import myConvexHull


#create a DataFrame
def createDataFrame(data):
  df = pd.DataFrame(data.data, columns=data.feature_names)
  df['Target'] = pd.DataFrame(data.target)
  return df

#visualisasi hasil ConvexHull
def visualisasiConvexHull(df,a,b):
  plt.figure(figsize = (10, 6))
  colors = ['b','r','g','c','m','y','k']
  plt.title(data.feature_names[a] + ' vs ' + data.feature_names[b])
  plt.xlabel(data.feature_names[a])
  plt.ylabel(data.feature_names[b])
  for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[a,b]].values
    hull = myConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
      plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i%7])
  plt.legend()
