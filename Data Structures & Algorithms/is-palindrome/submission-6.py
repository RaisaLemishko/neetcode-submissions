class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [char for char in s if char.isalnum()]
        start = 0
        end = len(filtered) - 1
        
        while end - start > 0:
            if filtered[start].lower() == filtered[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True

        