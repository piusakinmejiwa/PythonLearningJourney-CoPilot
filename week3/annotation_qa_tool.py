# Annotation QA Tool annotation_qa_tool.py

review = input("Enter your review")

score = int(input("Enter your Quality Score:  "))


print("---------------------------")
print("ANNOTATION REPORT")
print("---------------------------")
print()
print("Review: ")
print(review)

print()
print("Length Check")

if len(review) >= 10:
    print("PASS")
else:
    print("FAIL")
print()
print("Score:")
print(score)
print()
print("Quality:")
if score >= 90:
    print("Excellent, Well Done!")
elif score >= 80:
    print("Good Work")
elif score >= 70:
    print("Average Work")
elif score < 70:
    print("Poor")
else:
    print("Invalid Score Entry")
