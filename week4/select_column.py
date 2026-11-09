# Select a Column select_column.py
import pandas as pd

data = {
    "review": [

        "Excellent Service",
        "Poor Delivery",
        "Average Experience"
    ],
    "label": [
        "positive",
        "negative",
        "neutral"
    ]
}

df = pd.DataFrame(data)

print(df["review"])