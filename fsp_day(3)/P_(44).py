from collections import deque


s= deque([22, 33, 44, 56, 67])

s.appendleft(44)
print(s)

s.popleft()
print(s)