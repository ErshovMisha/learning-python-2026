class Solution:
    def containsDuplicate(self, nums) -> bool:
        k = set(nums)
        if len(k) == len(nums):
            return False
        else:
            return True
        

sol = Solution()
print(sol.containsDuplicate([1, 2, 3]))