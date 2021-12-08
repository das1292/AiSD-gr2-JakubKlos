from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None

    def __repr__(self):
        return str(self.value)

    def is_leaf(self):
        if self.left_child==None and self.right_child==None:
            return True
        else:
            return False

    def add_left_child(self,value:Any):
        self.left_child=BinaryNode(value)

    def add_right_child(self,value:Any):
        self.right_child=BinaryNode(value)

    def traverse_in_order(self,visit:Callable[[Any],None]):
        if self.left_child!=None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child!=None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self,visit:Callable[[Any],None]):
        if self.left_child!=None:
            self.left_child.traverse_post_order(visit)
        if self.right_child!=None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self,visit:Callable[[Any],None]):
        visit(self)
        if self.left_child!=None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child!=None:
            self.right_child.traverse_pre_order(visit)

    def show(self,value,level=0):
        if self.right_child:
            self.right_child.show(value,level+1)
        print(' '*7*level+'(',self.value,')'+'[')
        if self.left_child:
            self.left_child.show(value,level+1)