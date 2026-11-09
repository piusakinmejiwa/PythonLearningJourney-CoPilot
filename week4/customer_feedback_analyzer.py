# Customer Feedback Analyser customer_feedback_analyser.py

import pandas as pd

df = pd.read_csv("reviews.csv")

print("Customer Feedback Report")
print("------------------------")

print(f"Total Reviews: {len(df)}")
print()

print("Label Counts: ")
print(df["label"].value_counts())