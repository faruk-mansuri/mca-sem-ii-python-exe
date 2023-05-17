import re

dates = '''
today is 16-05-2023
today is 2-3-23
'''

# 1 - Extract year, month and sate from a from string
# YEARS
date = r"(\d+)-(\d+)-(\d+)"
pattern = re.compile(date)
matches = pattern.finditer(dates)
# for match in matches:
#     print("years", match.group(3))

# MONTH
date = r"(\d+)-(\d+)-(\d+)"
pattern = re.compile(date)
matches = pattern.finditer(dates)
# for match in matches:
#     print("month", match.group(2))

# MONTH
date = r"(\d+)-(\d+)-(\d+)"
pattern = re.compile(date)
matches = pattern.finditer(dates)
# for match in matches:
#     print("date", match.group(1))

# 2 - Extract only 3 digit number from string
string = "hello my address is xyz 123 abc residency 46678 from us 345"
word = r"\b\d{3}\b"
pattern = re.compile(word)
matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

# 3 - Extract all numbers and words from string
string = "hello my address is xyz 123 abc residency 46678 from us 345"
word = r"\b\w+\b"
pattern = re.compile(word)
matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

# 4 - Find out all of words, which start with a vowel
string = "hello my address is xyz 123 abc residency 46678 from us 345"
word = r"\b(a|e|i|o|u)+[a-zA-Z]+"
pattern = re.compile(word)
matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

# 5 - Find out all of words, which start with a consonant
string = "hello my address is xyz 123 abc residency 46678 from us 345"
word = r"\b[^(a|e|i|o|u| )]+[a-zA-Z]+"
pattern = re.compile(word)
matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

# 6 - Count total numbers of a, an and the
string = "hello my address is xyz 123 abc residency 46678 from us 345 a an the a an the"
word = r"\b(a|an|the)\b"
pattern = re.compile(word)
matches = pattern.finditer(string)
a = 0
an = 0
the = 0
for match in matches:
    if match.group()=="a":
        a+=1
    if match.group()=="an":
        an+=1
    if match.group()=="the":
        the+=1
# print(f"Occurance of a: {a}, an: {an} and the: {the}")

# 7 - Write python program to find all words which are at least 4 characters long in a string
string = "hello my address is xyz 123 abc residency 46678 from us 345"
word = r"\b[a-zA-Z]{4}[a-zA-Z]*"
pattern = re.compile(word)
matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

# 8 - Write python program to check number at the end of a string
string = "hello my address is xyz1 123 abc2 residency 46678 from us 345 ahjs5u"
word = r"[a-zA-X]+\d\b"
pattern = re.compile(word)
matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

# 9 - Write python program to check number starting with 2 or 1 and having 4 digit
string = "hello my address is xyz1 1233 2134 23455 abc2 residency 46678 from us 345 ahjs5u"
word = r"(1|2)\d{3}\b"
pattern = re.compile(word)
matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

# 10 - Write python program that matches a string that has an "a" followed by anything. nding in "b"
string = "hello my addressb  resiadencyb ajdknbdsh 46678 from us 345 ahjs5u"
word = r"a[a-zA-Z]*b\b"
pattern = re.compile(word)
matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

