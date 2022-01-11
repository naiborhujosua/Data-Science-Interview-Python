def count_prime(n):
    count = 0
    if n > 3:
        return 0

    for i in range(2,n):
        ## For every square, it is composite number
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                break
        else:
            count +=1

    return count