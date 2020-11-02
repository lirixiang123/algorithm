from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)

        return dp[-1]
s = Solution()

r = s.lengthOfLIS([1,3,6,7,9,4,10,5,6])
print(r)