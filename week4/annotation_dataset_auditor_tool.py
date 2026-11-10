# Annotation Dataset Auditor annotation_dataset_auditor.py

import pandas as pd

data = pd.read_csv("messy_reviews.csv")

df = pd.DataFrame(data)

null_counts = df["review"].isnull().sum()

total_rows = len(df)
duplicates = df.duplicated().sum()

print()
print("ANNOTATION DATASET AUDIT")
print("------------------------")
print()
print(f"Total Records:   {total_rows}")
print()
print(f"Missing Reviews: {null_counts}")
print()
print(f"Duplicate Records: {duplicates}")
print()
print(f"Invalid Labels: {null_counts}")

