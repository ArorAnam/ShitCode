def maxFrequency(nums: list, k: int) -> int:
    nums.sort()

    l, r = 0, 0
    res, total = 0, 0 # mac freq to return, total sum o fthe current window

    while r < len(nums):
        total += nums[r]

        while nums[r] * (r - l + 1) > total + k: # while window is invalid
            # shring the window
            total -= nums[l]
            l += 1
        
        res = max(res, r - l + 1)
        r += 1

    return res