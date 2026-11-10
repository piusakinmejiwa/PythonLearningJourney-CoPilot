# Drop Missing drop_missing.py

import pandas as pd

data = {
    "review": [
        "Excellent service",
        None,
        "Average Experience",
        "Poor Delivery"
    ],
    "label": [
        "positive",
        "negative",
        None,
        "negative"
    ]
}

df = pd.DataFrame(data)

clean_df = df.dropna()

print(clean_df)