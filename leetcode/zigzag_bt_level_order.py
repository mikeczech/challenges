from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = [[root.val]]
        queue = deque([root])

        zigzag_flag = True
        while True:
            level = []
            while queue:
                node = queue.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if not level:
                break
            if zigzag_flag:
                res.append([node.val for node in level][::-1])
            else:
                res.append([node.val for node in level])
            zigzag_flag = not zigzag_flag
            queue.extend(level)
        return res


def assert_equal(expected, val):
    try:
        assert expected == val
    except:
        print(f"{expected} != {val}")


assert_equal(
    [[3], [20, 9], [15, 7]],
    Solution().levelOrder(
        TreeNode(
            3,
            left=TreeNode(9),
            right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
        )
    ),
)
