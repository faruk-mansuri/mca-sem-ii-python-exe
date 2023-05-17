import random
import string


def accountNumber():
    randomString = random.choices(string.ascii_lowercase, k=10)
    randomNumber = list(str(random.randint(1000000000, 9999999999)))
    number = randomNumber+randomString
    random.shuffle(number)
    return "Id"+"".join(number)


print(accountNumber())
