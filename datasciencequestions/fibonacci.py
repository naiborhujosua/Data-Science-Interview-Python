"""Recursion Solution"""
def fibo_num(num):
    # 1,2,3,5
    if num==0 or num == 1 :
        return num
    return fibo_num(num-1) + fibo_num(num-2)

"""Brute Force Solution"""
def fibonacci(num):
    if num <=1:
        return num
    if num ==2:
        return num
    current =0
    previous1 =1
    previous2 =1

    for i in range(3,n+1):
        current = previous1 + previous2
        previous2 = previous1
        previous1 = current

    return current

