class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        
        for i in t:
            if i not in res:
                return False
            else:
                res[i] -= 1
                if (res[i] < 1):
                    del res[i]
        
        return not res