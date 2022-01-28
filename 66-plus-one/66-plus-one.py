class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_char = [str(num) for num in digits]
        num_str = int("".join(num_char)) + 1
        
        result =[]
        for i in str(num_str):
            result.append(int(i))
            
        return result
       
        
        
        
            
            
        