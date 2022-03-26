
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        n =len(s)
        dict ={}
        for i in range(n):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                dict[s[i]] =-1
                
        res = list(filter(lambda x : x >=0,dict.values()))
        return min(res) if res else -1
            
                
                
    
                
            
        
        