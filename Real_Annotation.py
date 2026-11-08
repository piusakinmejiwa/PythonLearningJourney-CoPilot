#Real_Annotation.py


reviews = ["Excellent Customer Support", "Terrible delivery experience", "Average product quality"]


labels  = ["Positive", "Negative", "Neutral"]

for review, label in zip(reviews, labels):
    print(f"Review: {review}\nAnnotation Label: {label}\n")




# for review in reviews:
#    for label in labels:
#        print(f"Review: {review}\nAnnotation Label: {label}")


# for review in reviews and label in labels:
#     print(review + label)