def findTargetSum(nums: list[int], target: int) -> int:
    dp = {} # (index, total_so_far) -> number_of_ways

    def backtrack(index, total):
        # base case
        if index == len(nums):
            return 1 if total == target else 0
        # check if already there
        if (index, total) in dp:
            return dp[(index, total)]
        
        dp[(index, total)] = backtrack(index + 1, total + nums[index]) + backtrack(index + 1, total - nums[index])

        return dp[(index, total)]
    
    return backtrack(0, 0)
    
nums = [1,1,1,1,1]
target = 3
res = findTargetSum(nums, target)
print(res)