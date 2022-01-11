def amstrong_num(nums):
    a = list(str(nums))
    b = 0
    for i in a:
        b += int(i)**len(a)
    
    return b == nums

print(amstrong_num(153))
