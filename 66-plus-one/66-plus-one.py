class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitLen = len(digits)
        allNines = True
        for digit in digits:
            if digit !=9:
                allNines =False
                break
                
        result = [None]*(digitLen +1) if allNines else [None]*digitLen
        
        sum = digits[digitLen-1]+1
        carry = sum//10
        result[len(result)-1] = sum%10
        
        ptr1 = digitLen -2
        ptr2 = len(result)-2
        
        while ptr1 >=0:
            sum = digits[ptr1]+carry
            carry = sum//10
            result[ptr2]= sum%10
            ptr1 -=1
            ptr2 -=1
            
        
        if allNines:
            result[0]=1
        
        return result 
            
        
        