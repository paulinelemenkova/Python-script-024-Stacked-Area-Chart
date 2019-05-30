#!/usr/bin/env python
# coding: utf-8

# In[42]:


# library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
#df.head(5)

#cmap = matplotlib.cm.Blues
#cmap_reversed = matplotlib.cm.get_cmap('autumn_r')


# Dataset
fig = plt.figure(figsize=(8, 6))

df = pd.DataFrame(data=df, columns=['Min', '1stQ', 'Median', 'Mean', '1stQ','Max']) 
ax = df.plot.area(stacked=False, alpha=0.8, colormap='PuBu_r')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Stacked area chart for the Mariana Trench bathymetry: \ndepths by 25 cross-section profiles', 
          fontsize=12, fontfamily='serif')

ax.set_xlabel('Bathymetric profiles')
ax.set_ylabel('Depths, m')
    
plt.xticks(np.arange(1, 26, step=1), rotation=30, )

plt.show()


# In[ ]:





# In[ ]:




