from collections import defaultdict
def findDuplicates(nums):

    counter = defaultdict(int)
    output =[]
    for num in nums:
        counter[num] +=1

    for key,value in counter.items():
        if value ==2:
            output.append(key)

    return output






