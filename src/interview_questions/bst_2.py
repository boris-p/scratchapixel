class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return str(self.val)


def insert(node: Node, val: int):
    if node is None:
        return Node(val)
    else:
        if node.val == val:
            return node
        elif val < node.val:
            node.left = insert(node.left, val)
        else:
            node.right = insert(node.right, val)
        return node


def delete(root: Node, val: int):
    if root is None:
        return root

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # one child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # two children
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root


def search(root: Node, val: int):
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)


def find_min(node: Node):
    curr = node
    while curr.left is not None:
        curr = find_min(curr.left)
    return curr


def traverse(root: Node):
    if root:
        traverse(root.left)
        print(root.val)
        traverse(root.right)


root = Node(50)
insert(root, 30)
insert(root, 80)
print("min is", find_min(root))
insert(root, 70)
insert(root, 20)
print("min is", find_min(root))
insert(root, 90)
traverse(root)

print("looking for 50:", search(root, 50))
print("looking for 25:", search(root, 25))

print("min is", find_min(root))


print("removing 20")
delete(root, 20)
traverse(root)

print("removing 50")
delete(root, 50)
traverse(root)
