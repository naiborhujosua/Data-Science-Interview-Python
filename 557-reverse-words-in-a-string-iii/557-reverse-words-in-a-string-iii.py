class Solution:
    def reverseWords(self, s: str) -> str:
        result =[]
        for i in s.split():
            result.append(i[::-1])
        return " ".join(result)
        