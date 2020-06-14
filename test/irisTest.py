'''
Created on 2018. 10. 31.

@author: molo
'''
import pandas as pd
from matplotlib import pyplot as plt
import sklearn.datasets

def get_iris_df():
    ds = sklearn.datasets.load_iris()
    df = pd.DataFrame(ds['data'], columns=ds['feature_names'])
    code_species_map = dict(zip(range(3), ds['target_names']))
    df['species'] = [code_species_map[c] for c in ds['target']]
    return df

df = get_iris_df()

sums_by_species = df.groupby('species').sum()
var = '꽃받침 너비(cm)'
sums_by_species[var].plot(kind='pie', fontsize=20)
plt.ylabel(var, horizontalalignment='left')
plt.title(var+'로 분류한 붓꽃', fontsize=25)
plt.savefig('iris_pie_for_one_variable.png')
plt.close()
