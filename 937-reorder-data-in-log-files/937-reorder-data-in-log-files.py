class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit =[]
        letters =[]
        for index,log in enumerate(logs):
            splitted = log.split(" ")
            id = splitted[0]
            type = splitted[1]
            
            if type.isnumeric():
                digit.append(log)
                
            else:
                letters.append((" ".join(splitted[1:]),id))
                
        letters.sort()
        
        return [id + " "  + other for other,id in letters ] + digit
    
        
            
            
        