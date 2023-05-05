def countOccurrence():
    str = input("Enter sentence: ")
    occurrence = {}
    for i in str:
     if not occurrence.get(i):
      occurrence[i] = 1
     else:
         occurrence[i]+=1

    for key, value in occurrence.items():
       print(f"{key} comes {value} times")

countOccurrence()