import queue


class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot: TreeNode)-> int:
        if not pRoot:
            return 0
        # 层序遍历(三种遍历方式 前 中 后)
        l = queue.Queue()
        res = 0
        l.put(pRoot)
        while not l.empty():
            n = l.qsize()
            for i in range(n):
                node = l.get()
                if node.left:
                    l.put(node.left)
                if node.right:
                    l.put(node.right)
            res += 1
        return res

    def TreeDepth1(self, pRoot: TreeNode)-> int:
        if not pRoot:
            # 当为空的时候终止递归
            return 0
        # 广度优先遍历(递归)
        return 1 + max(self.TreeDepth(self.TreeDepth1(pRoot.left)), self.TreeDepth(self.TreeDepth1(pRoot.right)))
