symbol = 64

for i in range(1, 5):
    pat = symbol + i
    for j in range(1,i+1):
        print(chr(pat), end=" ")
        pat+=1
    print()