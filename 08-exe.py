string = input("Enter string: ")
print(string[:])
print(string[::-1])
if string[:]==string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

