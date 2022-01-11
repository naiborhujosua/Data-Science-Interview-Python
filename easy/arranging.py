def arranging(n):

    left ,right = 0,n
    while left <=right:
        k = (left+right)//2
        current = k*(k+1)//2
        
        if current ==n:
            return k
        elif current > n:
            left = k+1
        else:
            right =k-1
    
    return right

