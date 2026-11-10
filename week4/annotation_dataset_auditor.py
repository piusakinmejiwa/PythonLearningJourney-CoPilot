# Annotation Dataset Auditor annotation_dataset_auditor.py

import pandas as pd

data = {
    "review": [
        "Excellent Service",
        None,
        "Poor Delivery",
        "Excellent Service",
        "Average Quality"
    ],
    "label": [
        "posiive",
        "negative",
        "negative",
        "positive",
        "good"
    ]

}

df = pd.DataFrame(data)

null_counts = df["review"].isnull().sum()



total_rows = len(df)
duplicates = df[df.duplicated()]
print(total_rows)
print(df)
print()
print("ANNOTATION DATASET AUDIT")
print("------------------------")
print()
print(f"Total Records:   {total_rows}")
print()
print(f"Missing Reviews: {null_counts}")
print()
print(f"Duplicate Records: {duplicates}")
print(duplicates.count())

