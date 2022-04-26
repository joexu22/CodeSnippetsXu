class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

pre_traversal = []
in_traversal = []
post_traversal = []

def preorder(root):
    if root is None:
        return

    pre_traversal.append(root.data)
    preorder(root.left)
    preorder(root.right)
    return pre_traversal

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    in_traversal.append(root.data)
    inorder(root.right)
    return in_traversal

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    post_traversal.append(root.data)
    return post_traversal




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)

print(inorder(root))