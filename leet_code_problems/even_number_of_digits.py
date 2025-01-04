# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

class Solution(object):
    def findNumbers(self, nums):
        return len([num for num in nums if len(str(num))%2 == 0])