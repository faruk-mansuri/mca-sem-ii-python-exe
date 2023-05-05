string1 = "hello jack"
string2 = "hello peter"
commonChar = set()

for i in range(len(string1)):
    # if string1[i]==" ": continue
    for j in range(len(string2)):
        if string1[i]==string2[j]:
            commonChar.add(string1[i])

print(commonChar)