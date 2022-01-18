from stack_queue.stack.structures import Queue


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

    assert queue.pop() == 1  #처음에 팝을 하면 1이 나와여야해
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None

    assert queue.is_empty()   ## 이게 True로 나와야해


test_queue()