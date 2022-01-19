class Node(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Linkedlist():
    def isPalindrome(head: ListNode) -> bool:
        q: list = []

        if not head:
            return True

        node = head
        print(node)
        print(type(node))

        while node is not None:
            q.append(node.val)
            node = node.next

        return True


end = Node()
n5 = Node(5, end)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

Linkedlist(n1)


####################

