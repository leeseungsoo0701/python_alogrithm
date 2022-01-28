class Node:
    def __init__(self,key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)



a = Node(3)
b = Node(9)
c = Node(-1)

a.next = b
b.next = c

#### 다 쓸수는 없다.
head