# Qualification check qualification_check.py

age = int(input("Enter your age:  "))

hours = int(input("Enter the number of hours you work per week:  "))

if age >= 18 and hours >= 10:
    print("You are qualified for the program.")
else:
    print("You are not qualified for the program.")