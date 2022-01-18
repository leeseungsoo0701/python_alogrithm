# 노드 생성
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self ,value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        topNode = self.top         #1. 가장 윗 접시를 꺼내서
        self.top = self.top.next  #3. 그 다음 4로 내려야한다
        return topNode.item   #2. 여기서 돌려준다

    def is_empty(self):
        return self.top is None


class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        pass

    def pop(self):
        pass

    def is_empty(self):
        return