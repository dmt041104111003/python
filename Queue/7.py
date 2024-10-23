from collections import deque  

def queue_after_n_rounds(n):  
    queue = deque([1, 2, 3, 4, 5])  
    for _ in range(n):  
        queue.append(queue.popleft())  
        queue.append(queue.popleft())  
    return queue[0]  