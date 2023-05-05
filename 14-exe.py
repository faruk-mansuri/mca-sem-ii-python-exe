list = [7,9,4,5,2,3]

def linearSearch(list, key):
    if key>=len(list) or key<0: return "Failure"
    for i in range(len(list)):
        if i==key: return "Success"

print(linearSearch(list, 3))
