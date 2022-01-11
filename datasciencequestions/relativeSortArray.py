from collections import defaultdict

def relativeSortArray(arr1,arr2):
    counter = defaultdict(int)
    new_1 =[]
    new_2 =[]
    for i in arr1:
        counter[i] +=1

    for i in arr2:
        if i in arr1:
            new_1.extend([i]*counter[i])

    for i in arr1:
        if i not in arr2:
            new_2.append(i)

    
    new_2.sort()

    return new_1 + new_2

