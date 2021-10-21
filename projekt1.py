from typing import Any

class Node:
    value: Any
    next: 'Node'

class LinkedList:
    head: Node
    tail: Node

    def __init__(self, list_) -> None:
        self.list_ = LinkedList()

    def __len__(self) -> int:
        return len(self.list_)

    def __push__(self, value: Any) -> None:
        assert list_.head == None

    def __append__(self, value: Any) -> None:
        list_.push(1)
        list_.push(0)
        assert str(list_) == '0 -> 1'

    def __node__(self, at: int) -> Node:
        list_.append(9)
        list_.append(10)

        assert str(list_) == '0 -> 1 -> 9 -> 10'

    def __insert__(self, value: Any, after: Node) -> None:
        middle_node = list_.node(at=1)
        list_.insert(5, after=middle_node)

        assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

    def __pop__(self) -> Any:
        first_element = list_.node(at=0)
        returned_first_element = list_.pop()

        assert first_element.value == returned_first_element

    def __remove_last__(self) -> Any:
        last_element = list_.node(at=3)
        returned_last_element = list_.remove_last()

        assert last_element.value == returned_last_element
        assert str(list_) == '1 -> 5 -> 9'

    def __remove__(self, after: Node) -> Any:
        second_node = list_.node(at=1)
        list_.remove(second_node)
        assert str(list_) == '1 -> 5'

lista: LinkedList=LinkedList(0,1)

len(lista)

