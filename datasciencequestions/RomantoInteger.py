
def romanToInt(S):
    roman = {'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000}
    ans = 0
    last ="I"
    for i in S[::-1]:
        if roman[i] < roman[last]:
             ans -= roman[i]
        else: 
            ans += roman[i]
        last = i
    return ans

