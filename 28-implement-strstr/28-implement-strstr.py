class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) ==0:
            return 0
        n = len(needle)
        h =len(haystack)
        
        if h < n:
            return -1
        for i in range(h-n +1):
            if haystack[i:i+n] == needle:
                return i
            
        return -1
        

            
    
        
    
        
        
                       
           
                       
                      