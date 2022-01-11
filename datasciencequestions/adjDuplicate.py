def adjDuplicate(s):
    result = []
    for i in s:
        if result and result[-1]==i:
            result.pop()
        else:
            result.append(i)

    return "".join(result)


