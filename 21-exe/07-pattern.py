
for i in range(1, 5):
    for j in range(1, i+1):
        if (i+j) % 2 == 0:
            symbol = "1"
        else:
            symbol = "0"
        print(symbol, end=" ")

    print()
