def uniqueString(s):

    for i in range(len(s)):
        alpha = s[i]
        if s.count(alpha) == 1:
            return i

    return -1