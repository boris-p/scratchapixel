class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(node: Node, key):
    # inserts node
    if node is None:
        return Node(key)
    else:
        if node.val == key:
            return node
        elif node.val < key:
            node.right = insert(node.right, key)
        else:
            node.left = insert(node.left, key)
    return node


def inorder_traverse(node: Node):
    # will print all the values in a sorted way
    if node:
        inorder_traverse(node.left)
        print(node.val)
        inorder_traverse(node.right)


def minValueNode(node: Node):
    current = node
    while(current.left is not None):
        current = current.left
    return current


def deleteNode(root: Node, key: int):
    # base case
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # one or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # two children
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root


def search(root, key):

    # base case - root is null or equals the key
    if root is None or root == key:
        return root

    # key is greater than the root
    if key > root:
        search(root.right, key)

    # key is smaller than the root
    search(root.left, key)


r = Node(50)
insert(r, 30)
insert(r, 20)
insert(r, 40)
insert(r, 70)
insert(r, 60)
insert(r, 80)
inorder_traverse(r)

print("deleting node 20")
deleteNode(r, 20)
inorder_traverse(r)

print("inserting node 20")
insert(r, 20)
inorder_traverse(r)

print("deleting node 40")
deleteNode(r, 40)
inorder_traverse(r)

print("deleting node 70")
deleteNode(r, 70)
inorder_traverse(r)
