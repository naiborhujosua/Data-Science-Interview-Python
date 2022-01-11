def factorial(nums):
    
    result = nums
    count = 0
    while nums > 1:
        result *= (nums-1)
        nums -= 1

    for i in str(result)[::-1]:
        if i == "0":
            count +=1
        else:
            break
    return count


print(factorial(5))
        









