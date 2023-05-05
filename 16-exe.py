def removeDuplicates():
    str = input("Enter sentence: ")
    str = helperFunction(str)
    str = str.split(" ")
    str.sort()
    str = " ".join(str)
    return str

def helperFunction(str):
    if len(str) == 1 : return str
    if str[0] == str[1] : return  helperFunction(str[1:])
    return str[0] + helperFunction(str[1:])

print(removeDuplicates())
