from collections import deque

s, t = map(str, input().split())

result = 'false'
def anagram(s: list[str], t: list[str]) -> bool:
    global result
    if sorted(s) == sorted(t):
        result = 'true'
        return result
    else:
        return result

print(anagram(s, t))
