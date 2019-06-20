#!/usr/bin/env python
# coding: utf-8
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
sns.set_context('paper')

# data frame
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
x = df.profile
y = [df.Min, df.Mean, df.Median, df.Max]
pal = sns.color_palette("ocean")

# plotting
plt.stackplot(x,y, labels=['Min', 'Mean', 'Median', 'Max'],
              colors=pal, alpha=0.4
              )
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Stacked area chart for the Mariana Trench bathymetry: \ndepths by 25 cross-section profiles',
          fontsize=12, fontfamily='serif')

# visualizing and saving
plt.tight_layout()
plt.savefig('plot_StackAreaA.png', dpi=300)
plt.show()
