from collections import deque

words = deque(input())
temp = []
while words:
    word = words.popleft()
