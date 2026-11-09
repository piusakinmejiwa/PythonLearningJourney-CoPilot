# Annotation Validator annotation_validator.py

label = int(input("Enter your label number from 1 to 3:  "))

if label == 1:
    print("Positive")
elif label == 2:
    print("Negative")
elif label == 3:
    print("Neutral")
else:
    print("Invalid Label")