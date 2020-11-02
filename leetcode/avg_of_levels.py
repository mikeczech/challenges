from typing import List, Dict
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RecursiveSolution:
    def collect_values(self, node: TreeNode, level: int, res: Dict[int, List[float]]):
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        if node.left:
            self.collect_values(node.left, level + 1, res)
        if node.right:
            self.collect_values(node.right, level + 1, res)

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        self.collect_values(root, 0, res)
        return [sum(values) / len(values) for values in res]


class BFSSolution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque([(root, 0)])
        res = []

        while queue:
            node, level = queue.popleft()
            if len(res) < level + 1:
                res.append([])
            res[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return [sum(values) / len(values) for values in res]


def assert_equal(expected, val):
    try:
        assert expected == val
    except:
        print(f"{expected} != {val}")

assert_equal([3, 14.5, 11], BFSSolution().averageOfLevels(TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))))
