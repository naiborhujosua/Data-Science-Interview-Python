class Solution:
    def climbStairs(self, n: int) -> int:
        case ={0:1,1:1}
        
        for i in range(2,n+1):
            case[i] = case[i-2] +case[i-1]
        return case[n]
            
            
             
                
    
            
            
        
        
        
        