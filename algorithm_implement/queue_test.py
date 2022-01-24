################ 먼저 들어간 놈이 나온다
######## 넣는 놈 node
from algorithm_implement.stack_implement import Node, Stack


def test_node():
    assert Node(1,None).item == 1  #### 노드를 만들어서 스택에 넣어보자 assert 보장한다 1에 해당하는 아이템 값이 1에 해당할 것 같아. Node의 값을 꺼내려면 .item


def test_queue():
    queue = Queue() ## stack을 만든다. stack은 3가지 기능이 필요하다.
    """
    1. push
    2. pop (접시 꺼내기)
    3. is_empty #비었는지 판단 유무 
    """
    queue.push(1)   #하나씩 넣어보자
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1  #처음에 queue를 pop하면 1이 나와야해
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()   ## 이게 True로 나와야해 (다 비웠으므로)


test_node()
test_queue()




