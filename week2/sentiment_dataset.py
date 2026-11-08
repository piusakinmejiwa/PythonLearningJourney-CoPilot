# sentment_dataset.py

reviews = ["Excellent Service", "Poor Support", "Amazing Product", "Bad Experience", "Aveage Quality"]

labels = ["Positive", "Negative", "Positive", "Negative", "Neutral"]

for review, label in zip(reviews, labels):
    print(f"Review: {review}\nLabel: {label}")

print("-------------------------------------------")
print(f"Total Reviews: {len(reviews)}")
print(f"Total Labels: {len(labels)}")