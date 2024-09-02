# grokking
def house_robber(money):
    if len(money) == 0 or money is None:
        return 0
    
    if len(money) == 1:
        return money[0]

    return max(house_robber_helper(money[:-1]), house_robber_helper(money[1:]))

def house_robber_helper(money):
    lookup_array = [0 for x in range(len(money) + 1)]
    lookup_array[0] = 0
    lookup_array[1] = money[0]

    for i in range(2, len(money) + 1):
        lookup_array[i] = max(money[i-1]+lookup_array[i-2], lookup_array[i-1])
    
    return lookup_array[len(money)]

def main():
    inputs = [[2,3,2], [1,2,3,1], [1,2,3,4,5,6,7,8,9,10,12,13,14,15], [7,4,1,9,3], []]

    for i in range(len(inputs)):
        print(i + 1, ".\tHouses: ", inputs[i], sep="")
        print("\n\tMaximum loot: ", house_robber(inputs[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()

# TIME: O(N), N is the length of the money array
# SPACE: O(N), N space is used by the lookup array
    

# NEETCODE
def rob(nums: List[int]) -> int:
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

def helper(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        newRob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2