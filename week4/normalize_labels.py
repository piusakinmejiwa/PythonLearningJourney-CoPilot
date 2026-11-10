# Normalize Labels normalize_labels.py

import pandas as pd

data = {
    "label": [
        "Positive",
        "NEGATIVE",
        "neutral",
        "Positive"
    ]
}

df = pd.DataFrame(data)

df["label"] = df["label"].str.lower()

print(df)