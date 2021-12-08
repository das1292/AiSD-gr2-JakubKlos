from BinaryNode import BinaryNode
from BinaryTree import BinaryTree

def bottom_line(tree:'BinaryTree'):
    list=[]
    root=tree.root

    def bottom_view(node:'BinaryNode'):
        if node.left_child:
            obc=node.left_child
            if obc.right_child==None:
                list.append(node.value)
        elif node.right_child:
            obc=node.right_child
            if obc.left_child==None:
                list.append(node.value)
        else:
            list.append(node.value)
    root.traverse_in_order(bottom_view)
    return list

tree = BinaryTree(10)

tree.root.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.left_child.right_child.add_right_child(7)
tree.root.left_child.add_left_child(2)
tree.root.left_child.left_child.add_right_child(5)
tree.root.left_child.left_child.add_left_child(4)
tree.root.left_child.left_child.left_child.add_right_child(9)
tree.root.left_child.left_child.left_child.add_left_child(8)

print(bottom_line(tree))

assert tree.root.value == 10
assert tree.root.left_child.right_child.value == 3
assert tree.root.left_child.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 2
assert tree.root.left_child.left_child.is_leaf() is False