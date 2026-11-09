# Feedback Classifier feedback_classifier.py

rating = int(input("Enter your rating (1-5): "))

if rating == 5:
    print("Excellent! Thank you for your feedback.")
elif rating == 4:
    print("Good! We appreciate your feedback.")
elif rating == 3:
    print("Average. We will strive to improve.")
elif rating <= 2:
    print("Poor")
else:
    print("Invalid rating. Please enter a number between 1 and 5.")