# Annotation Tool Version 1 annotation_tool_v1.py

review = input("Enter Review:  ")
score = int(input("Enter Quality Score:  "))

if score >= 90:
    print("Excellent Quality")
elif score >= 80:
    print("Good Quality")
elif score >= 70:
    print("Acceptable Quality")
elif score < 70:
    print("Needs Improvement")
else:
    print("Invalid Input")

# Let's check for the length of the review

if len(review) >= 10:
    print("Valid Review")
else:
    print("Review Too Short")