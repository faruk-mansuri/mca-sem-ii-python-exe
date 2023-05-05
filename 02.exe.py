def leapYear():
    year = int(input("Enter year: "))
    if year%4==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# leapYear()


def sumOfDigits(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    print(sum)

# sumOfDigits(10)