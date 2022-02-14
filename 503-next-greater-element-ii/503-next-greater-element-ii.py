class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result =[-1 for _ in range(len(nums))]
        stack =[]
        lnums= nums*2 
        n =len(nums)
        for i in range(len(lnums)):
            while len(stack) > 0  and stack[-1][0] < lnums[i]:
                val,pos = stack.pop()
                result[pos] = lnums[i]
                    
            if i < n:
                stack.append((lnums[i],i))
        
        return result
            
       
                    
                
        
        
        
        