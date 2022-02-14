class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        curr_even_sum = sum(x for x in nums if x %2 ==0)
        output =[]
       
        for value,index in queries:
            if nums[index]%2==0:
                curr_even_sum -=nums[index]
            nums[index] +=value
            
            if nums[index] %2 ==0:
                curr_even_sum +=nums[index]
                
            output.append(curr_even_sum)
            
        return output
            
           
            
       
            
            
        
        
            
            
    
                    
            
            
            
        
        