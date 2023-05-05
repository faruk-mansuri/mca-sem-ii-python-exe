def helperFunction(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True


def prime():
    n = int(input("Enter number: "))
    if n<2:
        print("Enter number bigger than 1")
        return
    
    if helperFunction(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")


prime()