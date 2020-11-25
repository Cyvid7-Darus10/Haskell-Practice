from abc import ABC,abstractmethod

class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def hasNext(self):
        pass

class Collection(ABC):
    @abstractmethod
    def newIterator(self):
        pass

class MyList(Collection):
    def __init__(self, elements: []):
        self.__elements = elements

    def size(self):
        return len(self.__elements)

    def elementAtIndex(self,index):
        return self.__elements[index]

    def newIterator(self):
        return ListIterator(self)


class MyBTree(Collection):
    def __init__(
                self, value: int, 
                left: 'MyBTree' = None, 
                right: 'MyBTree' = None
                ):
        self.__value = value
        self.__left = left
        self.__right = right

    def left(self):
        return self.__left

    def right(self):
        return self.__right

    def value(self):
        return self.__value

    def newIterator(self):
        return InOrderIterator(self)


class ListIterator(Iterator):
    def __init__(self, list: MyList):
        self.__traversedList = list
        self.__currentIndex = 0

    def next(self):
        self.__currentIndex += 1
        return self.__traversedList.elementAtIndex(self.__currentIndex-1)

    def hasNext(self):
        return self.__currentIndex < self.__traversedList.size()

class ReverseIterator(Iterator):
    def __init__(self, list: MyList):
        self.__traversedList = list
        self.__currentIndex = self.__traversedList.size()
    
    def next(self):
        self.__currentIndex -= 1
        return self.__traversedList.elementAtIndex(self.__currentIndex)

    def hasNext(self) -> bool:
        return self.__currentIndex > 0


class InOrderIterator(Iterator):
    def __init__(self, MyBTree: MyBTree):
        self.__traversedTree = MyBTree
        self.__stack = []
        self.__visited = []

        def inOrder(Node: MyBTree):
            if not Node:
                return
            inOrder(Node.left())
            self.__stack.append(Node.value())
            inOrder(Node.right())
            
        inOrder(self.__traversedTree)

    def next(self):
        return self.__stack.pop()

    def hasNext(self):
        return len(self.__stack)

class MyListReveresed(MyList):
    def newIterator(self):
        return ReverseIterator(self)

def main():
    c:Collection = MyList([1,2,3,4])
    iter:Iterator = c.newIterator()

    while(iter.hasNext()):
        print(iter.next())

    print("\n")

    c:Collection = MyListReveresed([1,2,3,4])
    iter:Iterator = c.newIterator()

    while(iter.hasNext()):
        print(iter.next())
    print("\n")

    c = MyBTree(10, MyBTree(3, right=MyBTree(4)), MyBTree(
        12, MyBTree(11, left=MyBTree(10)), MyBTree(14)))

#The Binary Tree
    """
             10
            /  \
           /    \ 
          3     12
           \    / \  
            4  11  14
              /
            10
    """

    iter:Iterator = c.newIterator()

    while(iter.hasNext()):
        print(iter.next())

if __name__ == "__main__":
    main()