from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    prereq = {c:[] for c in range(numCourses)}
    for crs, pre in prerequisites:
        prereq[crs].append(pre)
    
    # a course has 3 states
    # visited -> crs has been added to output
    # visiting -> crs not added to output, but added to cycle
    # univisited -> crs not addded to outout or cycle
    output = []
    visit, cycle = set(), set()
    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.add(crs)
        return True
        
    for c in range(numCourses):
        if not dfs(c):
            return []
    return output