# First Data Frame first_dataframe.py

import pandas as pd

data = {
    "review": [
        "Excellent Serice",
        "Poor Delivery",
        "Average experience"
    ],
    "label": [
        "positive",
        "negative",
        "neutral"
    ]
}

df = pd.DataFrame(data)

print(df)