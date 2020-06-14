'''
Created on 2018. 10. 29.

@author: molo
'''
import pandas as pd

df_w_age = pd.DataFrame({
    "name":["Tom","Tyrell","Janice"],
    "age":[60,25,33]
    })

df_w_height = pd.DataFrame({
    "name":["Tom","Tyrell","Janice"],
    "height":[6.2,4.0,5.5]
    })

joined = df_w_age.set_index("name").join(df_w_height.set_index("name"))
print(joined)

print("========================")

df = pd.DataFrame({
    "name":["Tom","Tyrell","Janice"],
    "age":[60,25,33],
    "height":[6.2,4.0,5.5],
    "gender":["M","M","F"]
    })

print(df.groupby("gender").mean())

print("==========")

medians = df.groupby("gender").quantile(0.5)
print(medians)

print("==========")

def agg(ddf):
    return pd.Series({
        "name":max(ddf["name"]),
        "oldest":max(ddf["age"]),
        "mean_height":ddf["height"].mean()
        })
print(df.groupby("gender").apply(agg))
