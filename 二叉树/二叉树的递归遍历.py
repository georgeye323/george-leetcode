"""
二叉树的遍历
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode):
    """
    二叉树的前序遍历
    :param root:
    :return:
    """
    result = []

    def traversal(root: TreeNode):
        if root is None:
            # 当root为空时候退出循环
            return
        result.append(root.val)
        traversal(root.left)
        traversal(root.right)
    traversal(root)
    return result


def inorder_traversal(root: TreeNode):
    """
    二叉树的中序遍历
    :param root:
    :return:
    """
    result = []

    def traversal(root: TreeNode):
        # 左 根 右
        if root is None:
            return
        result.append(root.left)
        result.append(root.val)
        result.append(root.right)
    traversal(root)
    return result


def postorder_traversal(root: TreeNode):
    """
    二叉树的后序遍历
    :param root:
    :return:
    """
    result = []

    def traversal(root: TreeNode):
        if root is None:
            return
        result.append(root.left)
        result.append(root.right)
        result.append(root.val)

    traversal(root)
    return result
