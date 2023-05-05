string = "hello,jack smith welcome,back to our home"
string = string.replace(",","-")

str = string.split(" ")

for i in range(len(str)):
    hyphen = "-"
    if hyphen in str[i]:
        words = str[i].split("-")
        words.sort()
        print(words)
    


