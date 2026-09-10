class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        
        if not s:
            return True

        for char in s:
            if (char in opening):
                res.append(char)
            else:
                if not res:
                    return False
                if (opening.index(res[-1]) == closing.index(char)):
                    res.pop()
                else:
                    return False
        
        if not res:
            return True
        else: 
            return False