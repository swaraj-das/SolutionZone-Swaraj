class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([x for x in nums if nums.count(x) == 1])
