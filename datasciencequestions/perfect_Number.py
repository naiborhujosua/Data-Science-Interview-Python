"""Solution 1"""
def perfectNumber(num):
    divisor =[]
    for i in range(1,num):
        if num%i ==0:
            divisor.append(i)

    return sum(divisor)== num


"""Solution 2"""
def perfect_number(num):
    if num <=1:
        return False

    divisor =set([1])

    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            divisor.add(i)
            divisor.add(num//i)

    return sum(divisor)==num


