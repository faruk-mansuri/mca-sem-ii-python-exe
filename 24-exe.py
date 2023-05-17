names = ['jack', "susan", "peter", "john", "johnson"]

def sortWithFunc(names):
    names.sort()
    return names

print("sort with function ", sortWithFunc(names))

def sortWithoutFunc(names):
    for i in range(len(names)-1,-1,-1):
       for j in range(i):
           swap = False
           if names[i] < names[j]:
                names[i], names[j] = names[j] ,names[i]
                swap = True
       
       if not swap :
           break
    
    return names

print("sort without function ",sortWithoutFunc(names))

