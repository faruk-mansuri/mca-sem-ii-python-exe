def sum():
    n = int(input("Enter number: "))
    oddSum = 0
    evenSum = 0

    for i in range(1, n+1):
        if i%2==0:
            evenSum+=i
        else:
            oddSum+=i

    print(f"odd sum of {n} is {oddSum}")
    print(f"even sum of {n} is {evenSum}")

sum()