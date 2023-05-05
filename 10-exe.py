string = "hello python"

def countVowel(str):
    vowelCount = 0
    consonantsCount = 0
    blankCount = 0
    for i in range(len(str)):
        if str[i].lower()=="a" or str[i].lower()=="e" or str[i].lower()=="i" or str[i].lower()=="o" or str[i].lower()=="u" or str[i].lower()==" ":
            vowelCount+=1
        elif str[i]==" ":
            blankCount+=1
        else:
            consonantsCount+=1
    return {"vowel":vowelCount, "consonants":consonantsCount, "blank":blankCount}

print(countVowel(string))