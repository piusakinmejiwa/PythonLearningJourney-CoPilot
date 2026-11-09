# Explore the datafram explore_dataframe.py

import pandas as pd

data = {

    "review": [
        "Excellent Service",
        "Poor delivery",
        "Average experience"
    ],
    "label": [
        "positive",
        "negative",
        "neutral"
    ]
}

df = pd.DataFrame(data)

print(df.head())
print()
print(df.columns)
print()
print(df.shape)