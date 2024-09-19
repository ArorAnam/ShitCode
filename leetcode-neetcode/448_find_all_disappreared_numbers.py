def findDisapperedNumbers(nums):
    # Time complexity: O(n)
    # Space complexity: O(1)
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])
    return [i+1 for i in range(len(nums)) if nums[i] > 0]

# Hashset solution
def findDisappearedNumbers(nums):
    # Time complexity: O(n)
    # Space complexity: O(n)
    num_set = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in num_set]