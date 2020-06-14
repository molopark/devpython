'''
Created on 2018. 10. 29.

@author: molo
'''

import pandas as pd

df = pd.DataFrame({
    "name":["Bob","Alex","Jane"],
    "age":[60,25,33]
    })

#other_df = pd.read_csv("myfile.csv")

df["age_plus_one"] = df["age"]+1
df["age_times_two"] = 2*df["age"]
df["age_squared"] = df["age"] * df["age"]
df["over_30"] = (df["age"]>30)

total_age = df["age"].sum()
print('1.total_age:%s' %total_age)

median_age = df["age"].quantile(0.5)
print('2.median_age:%s' %median_age)
print('=======')

df_below50 = df[df["age"]<50]
print(df_below50)
print('=======')

df["age_squared"] = df["age"].apply(lambda x:x*x)
df["age_plus_one"] = df["age"]+1
df["age_times_two"] = 2*df["age"]
df["age_squared"] = df["age"] * df["age"]
df["over_30"] = (df["age"]>30)

df_w_name_as_ind = df.set_index("name")
print(df_w_name_as_ind.index)

print('=======')

bobs_row = df_w_name_as_ind.loc["Bob"]
print(bobs_row["age"])

print('=======')

type(bobs_row)
print(bobs_row)
