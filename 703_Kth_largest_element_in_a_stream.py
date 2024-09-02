import heapq

class KthLargest:  
    
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = None
        self.k = k
        heapq.heapify(self, self.minHeap) # O(NlogN)
        while len(self.minHeap) > k:    # O((N-k)logN)
            heapq.heappop(self.minHeap) # O(logN)

    def add(self, val:int) -> int:
        heapq.heappush(self.minHeap, val) # O(logN)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)   # O(logN)
        return self.minHeap[0]
    
    # Time: O(NLogN)
    # Space: O(N)