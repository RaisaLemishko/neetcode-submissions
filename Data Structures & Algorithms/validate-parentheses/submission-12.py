class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        mapping = {
            ')': '(', 
            '}': '{', 
            ']': '['
            }
        
        if not s:
            return True

        for char in s:
            if (char in mapping):
                if (res and res[-1] == mapping[char]):
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
                
        
       
        return True if not res else False