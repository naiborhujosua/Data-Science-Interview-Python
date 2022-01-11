from collections import defaultdict
def repeatedNTimes(nums):
    counter = defaultdict(int)

    for num in nums:
        counter[num] +=1

    for key,value in counter.items():
        if value >=2:
            return key


