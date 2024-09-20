def singleNummber(nums: list[int]) -> int:
    if not nums:
        return 0
    
    result = 0
    
    for num in nums:
        result ^= num
    
    return