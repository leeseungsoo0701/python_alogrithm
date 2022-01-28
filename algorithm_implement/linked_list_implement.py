#Node의 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#linkedList 구현
class ListNode:
    def __init__(self, val):
        self.head = Node(val)

        # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
        def append(self, data):
            cur = self.head           ####### 우선 현재 head를 cur에 넣는다.
            while cur.next is not None:  ########## cur이 가르키는 다음 것이 None이 아니라면, 즉 다음을 가르키는 것이 있다면
                cur = cur.next           ######## 또 cur이 가르키는 다음것을 cur에 넣는다. 언제까지? None을 가르킬때까지
            cur.next = Node(data)       ###### 이제 cur.next가 None을 가르킬 때 Node(data)를 가르키드록, 즉 맨 뒤에 붙인다.

        # 모든 노드 값 출력
        def print_all(self):
            cur = self.head           ######### 현재 head를 cur에 넣는다.
            while cur is not None:    ######### cur이 None이 아니라면 즉 가르
                print(cur.data)
                cur = cur.next
