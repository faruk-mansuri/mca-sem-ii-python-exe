list = ["cba","abc"]

def sortFunction(list):
    ascList = list.copy()
    descList = list.copy()
    ascList.sort()
    descList.sort(reverse=True)
    
    if ascList == list:
        print("List is sorted in ascending order")
    elif descList == list:
        print("List is sorted in descending order")
    else:
        print("Items in list are not sorted")

sortFunction(list)






