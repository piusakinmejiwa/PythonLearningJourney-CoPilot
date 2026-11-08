#customer_feedback.py


reviews = ["Excellent Customer Support", "Terrible delivery experience", "Average product quality", "Great value for money"]

labels  = ["Positive", "Negative", "Neutral", "Excellent"]

for review, label in zip(reviews, labels):
    print(f"Review: {review}\nAnnotation Label: {label}\n")



