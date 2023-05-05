
def trianglePattern():
    for i in range(1, 5):
        for j in range(i, 5):
            print(" ", end=" ")

        for j in range(1, i+1):
            print("*", end=" ")

        for i in range(1, i):
            print("*", end=" ")
        print()


trianglePattern()
