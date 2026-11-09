# Job readiness job_readiness.py

training_days = int(input("How many days have you been training:  "))

no_of_projects = int(input("How many projects have you produced:  "))

if training_days >= 30 or no_of_projects >= 10:
    print("You are ready to start working professionally with Python")
else:
    print("You are not ready to start working professionally wth Python")