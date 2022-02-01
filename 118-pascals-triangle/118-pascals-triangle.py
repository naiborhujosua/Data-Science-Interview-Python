class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output =[[1]]
        for i in range(2,numRows+1):
            temp =[1]
            for j in range(1,i-1):
                temp.append(output[-1][j] + output[-1][j-1])
            temp.append(1)
            output.append(temp)
        return output
        
            
            
                
        