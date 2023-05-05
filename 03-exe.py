def grade():
    grade = int(input("Enter grade: "))

    if grade >= 80:
        print("O")
    elif grade >= 75:
        print("A+")
    elif grade >= 70:
        print("A")
    elif grade >= 65:
        print("B+")
    elif grade >= 60:
        print("B")
    elif grade >= 55:
        print("Pass")
    else:
        print("fail")
    
grade()