def sortColors(nums: List[int]) -> None:
    n = len(nums)
    count_map = {'0': 0, '1': 0, '2':0}
    for i in range(n):
        count_map[str(nums[i])] += 1
    i = 0
    for obj,counts in count_map.items():
        while counts:
            nums[i] = int(obj)
            i += 1
            counts -= 1
