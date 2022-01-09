def calPoints():
    result = []
    for i in ops:
        if i =="+":
            result.append(result[-1]+result[-2])
        elif i =="C":
            result.pop()
        elif i =="D":
            result.append(result[-1]*2)
        else:
            result.append(int(i))
                
    return sum(result)