# Missing Value missing_values.py

import pandas as pd

data = {
        "Reviews": [
            "Excellent Service",
            None,
            "Average experience",
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

print(df.isnull().sum())

