from typing import Any, List, Callable, Union

class Queue:
    def peek(self)->Any:
        return self.storage.head.value

    def enqueue(self, element: Any):
        self.storage.append(element)

    def dequeue(self)->Any:
        return self.storage.pop()

    def run(self, foo: Callable[['Any'], None]):
        while len(self)!=0:
            foo(self.dequeue())

    def __len__(self) -> int:
        return len(self._storage)

    def __repr__(self):
        out = []
        node = self._storage.head
        while node != None:
            out.append(node.value)
            node = node.next
        return out

    def __str__(self):
        str_out = map(str, self.__repr__())
        return ", ".join(str_out)


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value=None):
        self.value=value
        self.children=[]

    def __str__(self)->str:
        return str(self.value)

    def is_leaf(self)->bool:
        if len(self.children) == 0:
            return False
        else:
            return True

    def add(self, child: 'TreeNode'):
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        visit(self)

        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        visit(self)
        queue: 'Queue'=Queue()

        for i in self.children:
            queue.enqueue(i)

        while len(queue)!=0:
            a=queue.dequeue()
            visit(a)
            for i in a.children:
                queue.enqueue(i)

    def search(self,value: Any) -> Union['TreeNode',List['TreeNode'], None]:
        result: List[TreeNode]=[]

    def search_foo(node: 'TreeNode'):
        if node.value==value:
            result.append(node)

    self.for_each_level_order(search_foo)

    if len(result)==0:
        return None
    elif len(result)==1:
        return result[0]

    def foo(tree: 'TreeNode'):
        print(tree.node)



tree: 'TreeNode'=TreeNode(2)
tree.add(TreeNode(3))
tree.add(TreeNode(6))
tree.children[0].add(TreeNode(1))
tree.children[1].add(TreeNode(2))