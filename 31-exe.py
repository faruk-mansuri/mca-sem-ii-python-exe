import re

# 1 - Write a Puthon program to remove the parenthesis area in a string
# sample data -    ["example(.com)", "iicmr", "google(.com)", "youtube(.com)"]
# expected output  -  example   iicmr   google   youtube
urls = '''
example(.com)
iicmr
google(.com)
youtube(.com)
'''
word = r"([a-zA-Z]+)(\(.com\))?"
pattern = re.compile(word)
matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group(1))

# 2 - write a regular expression to extract the beggining word
data = "hello jack! how are you"
pattern = re.compile(r"^[a-zA-Z]+")
matches = pattern.finditer(data)
# for match in matches:
#     print(match.group())

# 3 - write a regular expression to extract first two characters from each word(not the number)
data = "hello jack! how are you 34475 random text 12382"
pattern = re.compile(r"\b[a-zA-Z]+")
matches = pattern.finditer(data)
# for match in matches:
#     print(match.group()[0:2])

# 4 - write a regular expression to extract date
data = "hello jack! how are you! today is 16-05-2023 and tommorrow is 17-05-23"
pattern = re.compile(r"\d{1,2}-\d{1,2}-\d{2,4}")
matches = pattern.finditer(data)
# for match in matches:
#     print(match.group())

# 5 - write a regular expression to extract date
data = "time is 16:33:18 after 10 minutes time is 16-43-18"
pattern = re.compile(r"\d{1,2}(-|:)\d{1,2}(-|:)\d{1,2}")
matches = pattern.finditer(data)
# for match in matches:
#     print(match.group())

# 6 - write a regular expression to extract valid IP address in python
ip = '''
192.168.0.1
181.11.25.225
11.32.81
'''
pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
matches = pattern.finditer(ip)
# for match in matches:
#     print(match.group())


# 7 - write re to validate email
email = '''
PeterParker@gmail.com
Peter.Parker@university.edu
Peter-321-parker@my-work.net
Peter.Parker@.edu
Peter-321-parker@my-work
Peter-321-parkermy-work.net
'''
pattern = re.compile(r"[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+\.(com|net|edu)")
matches = pattern.finditer(email)
# for match in matches:
#     print(match.group())

# 8 - write re to validate url
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://www.nasa
http://nasa
'''
pattern = re.compile(r"(http|https)://(www.)?[a-zA-Z0-9]+\.(com|gov|in)")
matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group())

# 9 - write re to validate PAN card number alpanumeric aord of the form AAAAA1111A
# where A denotes any letter of english ypparcase alphabets
# 1 denotes any digit in 0-9
# fourth character can be only from set{A,B,C,F,G,H,L,J,P,T,K}
pan_number = '''
ABCBY3678A
617T33678Z
ABC7Y36781
'''
pattern = re.compile(r"[A-Z]{3}(A|B|C|F|G|H|L|J|P|T|K)[A-Z]\d{4}[A-Z]")
matches = pattern.finditer(pan_number)
# for match in matches:
#     print(match.group())
