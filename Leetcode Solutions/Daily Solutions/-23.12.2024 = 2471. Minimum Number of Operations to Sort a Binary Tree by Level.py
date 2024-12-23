# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root):
        if not root:
            return 0
        
        from collections import deque
        q = deque([root])
        operations = 0

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            sort_level = sorted(level)
            mp = {v: i for i, v in enumerate(level)}

            for i in range(len(level)):
                while level[i] != sort_level[i]:
                    operations += 1
                    cur = mp[sort_level[i]]
                    mp[level[i]] = cur
                    level[i], level[cur] = level[cur], level[i]

        return operations
        