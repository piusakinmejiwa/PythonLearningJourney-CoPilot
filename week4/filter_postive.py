# Filter Postiive filter_positive.py

import pandas as pd

data = {
    "review": [
        "Excellent Service",
        "Poor Delivery",
        "Amazing Support",
        "Bad Experience"

    ],
    "label": [
        "positive",
        "negative",
        "positive",
        "negative"
    ]
}

df = pd.DataFrame(data)

positive_reviews = df[df["label"] == "positive"] 

print(positive_reviews)