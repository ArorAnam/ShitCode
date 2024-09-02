class Duplicate:
    def removeDuplicates(self, num: list[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] = '_'
        print(nums)
        
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != '_':
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        
        for i in nums:
            if i != '_':
                count += 1
        
        return count

        # Time: O(n)
        # Space: O(1)
            
# Test cases:
'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

[0,_,1,_,_,_,2,_,3,_,4]
    l,r
[0,1,(l)_,_,_,_,2(r),_3,_,4]

'''

