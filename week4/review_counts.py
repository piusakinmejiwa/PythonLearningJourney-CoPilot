# Review Count  revieww_counts.py

import pandas as pd

data = {
    "review": [
        "Excellent Service",
        "Poor Delivery",
        "Amazing Support",
        "Bad Experience",
        "Average Quality"
    ],
    "label": [
        "positive",
        "negative",
        "positive",
        "negative",
        "neutral"
    ]
}

df = pd.DataFrame(data)

print(df["label"].value_counts())
