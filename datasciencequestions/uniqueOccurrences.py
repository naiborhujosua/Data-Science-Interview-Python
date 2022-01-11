from collections import defaultdict
def uniqueOccurrences(arr):

    counter =defaultdict(int)

    for num in arr:
        counter[num] +=1

    return len(set(counter.values())) == len(counter.values())


    