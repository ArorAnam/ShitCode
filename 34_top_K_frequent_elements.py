# Solution 1: Max Heap
# Time: klog(n)

# Solution 2: Bucket Sort variation

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    frequency = [[] for i in range(len(nums) + 1)]

    # coutt elements
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    # put in frequency bucket
    for n, c in count.items():
        frequency[c].append(n)
    
    res = []
    for i in range(len(frequency) - 1, 0, -1):
        for n in frequency[i]:
            res.append(n)
            if len(res) == k:
                return res
    
    # Time: O(n)
    # Space: O(n)