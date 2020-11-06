from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ins = {c:[] for c in range(numCourses)} 
        outs = {c:[] for c in range(numCourses)} 
        for p in prerequisites: # O(E)
            source, target = p[0], p[1]
            ins[target].append(source)
            outs[source].append(target)

        in_deg = {c:len(v) for c,v in ins.items()}
        initial_courses =  [c for c in in_deg if in_deg[c] == 0]
        if not initial_courses:
            return False

        for c in initial_courses: # O(V)
            queue = deque([c]) # O(V + E)
            while queue:
                course = queue.popleft()
                for d in outs[course]:
                    in_deg[d] -= 1
                    if in_deg[d] == 0:
                        queue.append(d)

        return all([v <= 0 for v in in_deg.values()])

def assert_equal(expected, val):
    try:
        assert expected == val
    except:
        print(f"{expected} != {val}")

assert_equal(True, Solution().canFinish(2, [[1,0]]))
assert_equal(False, Solution().canFinish(2, [[1,0],[0,1]]))
assert_equal(True, Solution().canFinish(3, [[1,0],[2, 0]]))
assert_equal(True, Solution().canFinish(3, [[0,1],[0,2],[1,2]]))
assert_equal(False, Solution().canFinish(3, [[0,2],[1,2],[2,0]]))
assert_equal(True, Solution().canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))
assert_equal(True, Solution().canFinish(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))
