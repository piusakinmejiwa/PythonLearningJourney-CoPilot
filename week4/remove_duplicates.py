# Remove Duplicates remove_duplcates.py

import pandas as pd

data = {
    "review": [
        "Excellent Service",
        "Poor Delivery",
        "Excellent Service",
        "Average Quality"         

    ],
    "label": [
        "positive",
        "negative",
        "positive",
        "neutral"
    ]
}

df = pd.DataFrame(data)

clean_df = df.drop_duplicates()
print(clean_df)