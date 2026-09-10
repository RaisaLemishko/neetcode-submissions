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
            if (char in mapping.values()):
                res.append(char)
            else:
                if not res:
                    return False
                if (res[-1] == mapping[char]):
                    res.pop()
                else:
                    return False
        
        if not res:
            return True
        else: 
            return False