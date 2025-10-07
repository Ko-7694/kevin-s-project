marks = input("what is your marks? ")
marks = float(marks)
if marks < 40:
    print("fail")
if marks >= 40 and marks <= 59:
    print("pass")
if marks >= 60 and marks <= 79:
    print("credit")
if marks > 80:
    print("distinction")
