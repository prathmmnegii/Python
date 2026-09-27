class Solution(object):
    def containsDuplicate(self, nums):

        seen = set()

        for n in nums:
                seen.add(n)
        
        if len(nums) > len(seen):
            return True

        elif len(nums) == len(seen):
            return False
    