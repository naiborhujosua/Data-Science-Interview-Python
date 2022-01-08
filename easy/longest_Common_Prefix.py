def longest_Common_Prefix(strs):
    
    if not strs:
        return ""

    short_str = min(strs,key=len)

    for i, char in enumerate(short_str):
        for other in strs:
            if other[i] != char:
                return short_str[:i]

    return short_str 
