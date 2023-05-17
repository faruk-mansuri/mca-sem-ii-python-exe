def hill(list):
    max_element = max(list)

    for i in range(list.index(max_element)-1,0,-1):
        if list[i]<list[i-1]: return False
    
    for i in range(list.index(max_element)+1,len(list)-1,1):
        if list[i]<list[i+1]: return False

    return True

def valley(list):
    min_element = min(list)
    
    for i in range(list.index(min_element)-1,0,-1):
        if list[i]>list[i-1]: return False

    for i in range(list.index(min_element)+1,len(list)-1,1):
        if list[i]>list[i+1]: return False

    return True



def hillValley():
    n = int(input("How many element do you want in your list: "))
    list = [None]*n
    for i in range(n):
        list[i] = int(input("Enter number: "))

    if len(list) < 4: return

    print(f"Your list is: {list}")
    if hill(list): return "hill"
    elif valley(list): return "Valley"
    else:
        return "hill-valley"

print(hillValley())

