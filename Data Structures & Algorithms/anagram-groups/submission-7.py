class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            if ''.join(sorted(s)) in res:
                res[''.join(sorted(s))] = res[''.join(sorted(s))] + [s]
            else:
                res[''.join(sorted(s))] = [s]
        return list(res.values())
        


        