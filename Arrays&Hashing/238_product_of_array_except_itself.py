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