def result():
    AIT = int(input("Enter marks for AIT: "))
    Python = int(input("Enter marks for Python: "))
    SE = int(input("Enter marks for SE: "))
    OT = int(input("Enter marks for OT: "))
    ADBMS = int(input("Enter marks for ADBMS: "))

    return ((AIT+Python+SE+OT+ADBMS)/500)*100

print(result())