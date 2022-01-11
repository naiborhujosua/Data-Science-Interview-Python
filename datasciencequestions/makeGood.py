def makeGood(s):

    result = []

    for i in s:
        if result and ord(result[-1])== ord(i)+32 or ord(result[-1])== ord(i)-32:
            result.pop()
        else:
            result.append(i)

    return result



