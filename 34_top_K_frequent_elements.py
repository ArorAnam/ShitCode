"""
Problem: Top K Frequent Elements
Difficulty: Medium
Link: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Approach 1: Bucket Sort
    - Create a frequency map using a dictionary
    - Create buckets (list of lists) where index represents frequency
    - Place numbers in their frequency buckets
    - Collect k most frequent elements by iterating from highest frequency
    Time: O(n) where n is the length of nums
    Space: O(n) for both hashmap and bucket list

Approach 2: Heap (Min-Heap)
    - Count frequencies using Counter
    - Maintain a min-heap of size k
    - For each number-frequency pair:
        * If heap size < k: add to heap
        * If current frequency > smallest in heap: replace smallest
    Time: O(n log k) where n is the length of nums
    Space: O(n) for counter + O(k) for heap
"""

from typing import List
import heapq
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Bucket sort approach to find k most frequent elements.
    
    Args:
        nums: List of integers
        k: Number of most frequent elements to return
    
    Returns:
        List of k most frequent integers
    """
    # Initialize frequency map and bucket list
    count = {}
    frequency = [[] for _ in range(len(nums) + 1)]

    # Count frequency of each number
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    # Place numbers in their frequency buckets
    for n, c in count.items():
        frequency[c].append(n)
    
    # Collect k most frequent elements
    res = []
    for i in range(len(frequency) - 1, 0, -1):
        for n in frequency[i]:
            res.append(n)
            if len(res) == k:
                return res
    
    return res  # In case k is larger than unique numbers

def topKFrequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Min-heap approach to find k most frequent elements.
    
    Args:
        nums: List of integers
        k: Number of most frequent elements to return
    
    Returns:
        List of k most frequent integers
    """
    # Count the frequency of each number
    count = Counter(nums)
    
    # Maintain a min-heap of size k
    heap = []
    for num, freq in count.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, num))
    
    # Extract the k most frequent elements
    return [num for freq, num in heap]

# Example usage and testing
if __name__ == "__main__":
    test_cases = [
        ([1,1,1,2,2,3], 2),
        ([1], 1),
        ([1,2], 2)
    ]
    
    for nums, k in test_cases:
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Bucket Sort Output: {topKFrequent(nums, k)}")
        print(f"Heap Output: {topKFrequent_heap(nums, k)}\n")