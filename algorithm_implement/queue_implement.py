# 노드 생성
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Queue:

    ##### 생성 될 때는 front가 None인 상태
    def __init__(self):
        self.front = None


    #### Push를 하려면 우선 지금 value를 넣고 self의 top 즉 가장 최근에 넣은 것들의 경로를 넣어준다.
    #### 5는 4를 가르키고 4는 3을 가르키고.... 1은 None을 가르킨다.
    def push(self ,value):

        #front에 아무것도 없다면 맨 처음으로 넣어주면 된다.
        if not self.front:
            self.front = None(value,None)
            return

        #아니라면 우선 node에 front를 넣어놓고
        #node.next를 node에 넣어줘서 계속 타고타고 내려간다 (언제까지? node.next가 존재할때까지 즉 두번째 까지 이어준다)
        node = self.front
        while node and node.next:
            node = node.next

        node.next = Node(value,None)


    ### Pop을 할 때는 우선 front가 존재하는지 확인하고
    ### top에 있다면 출력하고 없다면 return None을 해준다.
    def pop(self):
        if self.front is None:
            return None

        Nodeitem = self.front         #1. 가장 윗 접시를 꺼내서(5와 4를 향하는 경로)
        self.front = self.front.next  #3. 그 다음 4로 내려야한다 그리고 top이 가르키는 경로를 5에서 4로 바꿔줘야한다.
        return Nodeitem.item   #2. return 5를 해준다


    def is_empty(self):
        return self.front is None    #front가 없다면 true, 있다면 False를 반환한다.