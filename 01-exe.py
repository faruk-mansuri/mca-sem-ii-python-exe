# 1
def evenOdd():
    num = int(input("Enter number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")

# evenOdd()

# 2


def GCD(a, b):
    if a < b:
        [a, b] = [b, a]
    if a % b == 0:
        return b
    return GCD(b, a % b)

# print(GCD(10,5))
