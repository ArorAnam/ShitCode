class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]

        for idx in range(1, len(nums)):
            if dp[idx - 1] > 0:
                dp[idx] = dp[idx - 1] + nums[idx]
            else:
                dp[idx] = nums[idx]
            if dp[idx] > max_sum:
                max_sum = dp[idx]

        return max_sum
