def leastInterval(tasks, n):
    task_map = {}
    for task in tasks:
        if task not in task_map:
            task_map[task] = 0
        task_map[task] += 1

    task_map = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
    max_val = task_map[0][1] - 1
    idle_slots = max_val * n

    for i in range(1, len(task_map)):
        idle_slots -= min(max_val, task_map[i][1])

    return len(tasks) + max(0, idle_slots)