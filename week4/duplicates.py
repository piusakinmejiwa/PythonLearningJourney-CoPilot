# Duplicates duplicates.py

import pandas as pd

data = {
    "review": [
        "Excellent Service",
        "Poor Delivery",
        "Excellent Service",
        "Average Quaity"

    ],
    "label": [
        "posiive",
        "negative",
        "positive",
        "neutral"
    ]
}

df = pd.DataFrame(data)

print(df.duplicated().sum())