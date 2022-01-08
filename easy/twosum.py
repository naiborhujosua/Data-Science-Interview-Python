def two_sum(nums,target):
    result = {}
    for i,num in enumerate(nums):
        comp = target-num
        if comp in result:
            return [result[target-num],i]
        result[num] = i
    return []

    
list =[1,3,5,6]
target = 8
print(two_sum(list,target))

