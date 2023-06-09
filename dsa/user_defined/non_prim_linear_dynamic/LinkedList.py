class _Node:
    __slots__ = '_element', '_next'

    def __init__(self,element,next):
        self._element=element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self,e):
        newest =_Node(e,None)

        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        while(p):
            print(p._element, end= "-->")
            p = p._next
        print()


list = LinkedList()
list.addlast(1)
list.addlast(2)
list.addlast(3)
list.display()
print("size:", len(list))


