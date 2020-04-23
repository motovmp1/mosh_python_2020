from collections import deque

queue = deque([10, 20, 30])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
queue.popleft()
if not queue:
    print("empty")
else:
    print(queue)