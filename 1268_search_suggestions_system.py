from typing import List
from bisect import bisect_left

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    # Time complexity: O(nlogn + n * m), where n is the number of products and m is the length of searchWord`
    # Space complexity: O(n)
    products.sort()
    res = []
    prefix = ''
    for c in searchWord:
        prefix += c
        i = bisect_left(products, prefix)
        res.append([product for product in products[i:i + 3] if product.startswith(prefix)])
    return res

    # Explaination of only bisect_left:
    # Bisect_left returns the index where the element should be inserted in the sorted list to maintain the order
    # Time compleity of bisect_left is O(logn)
    

# Alternate solution, implement manually, using two pointers
def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    res = []
    prefix = ''
    left, right = 0, len(products) - 1
    for c in searchWord:
        prefix += c
        while left <= right and (not products[left].startswith(prefix) or (products[left].startswith(prefix) and left < len(products) - 1 and products[left + 1].startswith(prefix))):
            left += 1
        while left <= right and (not products[right].startswith(prefix) or (products[right].startswith(prefix) and right > 0 and products[right - 1].startswith(prefix))):
            right -= 1
        res.append([product for product in products[left:min(left + 3, right + 1)]])
    return res

def suggestedProducts_final(products: List[str], searchWord: str) -> List[List[str]]:
    # Time complexity: O(nlogn + n * m), where n is the number of products and m is the length of searchWord
    # Space complexity: O(n)
    res = []
    products.sort()
    
    l, r = 0, len(products) - 1
    for i in range(len(searchWord)):
        c = searchWord[i]

        while l <= r and (len(products[l]) <= i or products[l][i] != c):
            l += 1
        while l <= r and (len(products[r]) <= i or products[r][i] != c):
            r -= 1
        
        res.append([])
        remaining = r - l + 1
        for j in range(min(3, remaining)):
            res[-1].append(products[l + j])
    
    return res

    # Explaination of this solution:
    # 1. Sort the products list
    # 2. Initialize two pointers l and r to the start and end of the products list
    # 3. Iterate over the searchWord
    # 4. For each character c in the searchWord:
    # 5. While l <= r and the l-th product does not have the c-th character as c, increment l
    # 6. While l <= r and the r-th product does not have the c-th character as c, decrement r
    # 7. Append an empty list to the result list
    # 8. Iterate over the range of min(3, r - l + 1):
    # 9. Append the product at index l + j to the last list in the result list
    # 10. Return the result list
