class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr =[]
        count =0
        
        for i in s:
            if i in arr:
                count = max([len(arr),count])
                index = arr.index(i)
                arr = arr[index+1:]
    
            arr.append(i)
        return max(len(arr),count)
       
        