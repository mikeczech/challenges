from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = {c:[] for c in range(numCourses)}
        in_deg = {c:0 for c in range(numCourses)}
        for target, source in prerequisites:
            out[source].append(target)
            in_deg[target] += 1

        initial_courses = [c for c, num_preq in in_deg.items() if num_preq == 0]
        if not initial_courses:
            return []

        res = []
        for c in initial_courses:
            queue = deque([c])
            while queue:
                course = queue.popleft()
                res.append(course)
                for d in out[course]:
                    in_deg[d] -= 1
                    if in_deg[d] == 0:
                        queue.append(d)
        if len(res) == numCourses:
            return res
        else:
            return []


def assert_equal(expected, val):
    try:
        assert expected == val
    except:
        print(f"{expected} != {val}")

assert_equal([0, 1], Solution().findOrder(2, [[1,0]]))
assert_equal([0,2,1,3], Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
