def finMin(nums: list) -> int:
    # Ex. [4,5,6,7,0,1,2,3]
    #      l     m       r
    #              l    r
    #              l r          
    #              lr

    n = len(nums)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    
    return nums[left]

    # Time: O(logN)
    # Space: O(1)

           