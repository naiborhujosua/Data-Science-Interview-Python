# Solution 
def isPalindrome(num):
    if num < 0:
        return False
    w = []

    for i in str(x)[::-1]:
        w.append(i)

    return "".join(w) == str(x)