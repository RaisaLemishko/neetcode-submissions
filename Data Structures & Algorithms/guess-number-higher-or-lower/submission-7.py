# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            med = (low + high) // 2

            if guess(med) < 0:
                #guess is higher
                high = med - 1
            elif guess(med) > 0:
                #guess is lower
                low = med + 1
            else:
                return med
        return -1