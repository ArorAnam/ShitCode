# minimum cost to reach the tp of the floor

# neetcode
def minCostClimbingStairs(cost: List[int]) -> int:
    # [10, 15, 20] 0
    cost.append(0)

    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])

    return min(min(cost[0], cost[1]))