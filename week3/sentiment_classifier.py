# Sentiment Classifer sentiment_classifier.py

sentiment = int(input("Enter your sentiment no which is from 1 to 3:  "))

if sentiment == 1:
    print("Positive")
elif sentiment == 2:
    print("negative")
elif sentiment == 3:
    print("neutral")
else:
    print("Invalid Selection")