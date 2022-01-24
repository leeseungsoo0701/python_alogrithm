################ 먼저 들어간 놈이 나온다
######## 넣는 놈 node
from algorithm_avatar.stack_implement import Node, Stack


def test_node():
    assert Node(1,None).item == 1  #### 노드를 만들어서 스택에 넣어보자 assert 보장한다 1에 해당하는 아이템 값이 1에 해당할 것 같아. Node의 값을 꺼내려면 .item


def test_stack():
    stack = Stack() ## stack을 만든다. stack은 3가지 기능이 필요하다.
    """
    1. push
    2. pop (접시 꺼내기)
    3. is_empty #비었는지 판단 유무 
    """
    stack.push(1)   #하나씩 넣어보자
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5  #처음에 팝을 하면 5가 나와여야해
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None

    assert stack.is_empty()   ## 이게 True로 나와야해


test_node()
test_stack()




