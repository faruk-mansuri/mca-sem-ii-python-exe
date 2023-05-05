
for i in range(1, 9):
    for j in range(i, 9):
        print("*", end="")

    for j in range(2, i+1):
        print("_", end="")

    for j in range(2, i+1):
        print("_", end="")

    for j in range(i, 9):
        print("*", end="")

    print()
