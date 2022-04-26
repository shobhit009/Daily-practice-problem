class Solution:
    def isValid(self, s: str) -> bool:
        
        buffer = []
        valueDictionary ={'(':')','{':'}','[':']'}
        
        for c in s:
            if c in valueDictionary:
                buffer.append(c)
            elif len(buffer) == 0 or valueDictionary[buffer.pop()] != c:
                return False
            
        return len(buffer) == 0    
        
        