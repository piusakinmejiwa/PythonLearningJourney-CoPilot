# Validate Labels validate_labels.py

import pandas as pd

data = {
    "review": [
        "Excellent Service",
        "Poor Delivery",
        "Average Quality",
        "Amazing Support"
    ],
    "label": [
        "positive",
        "negative",
        "good",
        "positive"
    ]
}

df = pd.DataFrame(data)

valid_labels = [
    "positive",
    "negative",
    "neutral"
]

invalid = df[
    ~df["label"].isin(valid_labels)
]

print(invalid)