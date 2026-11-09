# Annotation Access annotation_access.py

weeks_completed = int(input("Enter the number of weeks you have completed:  "))

study_hours = int(input("Enter the number of study hours you have completed:  "))

if weeks_completed >= 3 or study_hours >= 15:
    print("You are eligible for the next module.")
else:
    print("You are not eligible for the next module")