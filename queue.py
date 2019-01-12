from collections import deque
queue=deque(["anu","gowtham","sathya","shriya"])
print(queue)
queue.append("yogasundari")
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
