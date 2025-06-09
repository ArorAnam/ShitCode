def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    left = 1
    right = 1
    for i in range(n):
        res[i] *= left
        res[n - 1 - i] *= right
        left *= nums[i]
        right *= nums[n - 1 - i]
    return res

# Time: O(n)
# Space: O(1)

# alternate solution
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res