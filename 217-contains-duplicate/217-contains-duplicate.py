from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter =defaultdict(int)
        
        for i in nums:
            counter[i] +=1
        output =False
        for index,values in counter.items():
            if values >= 2:
                output=True
                break
        return output
            
            
        