from collections import deque  

def first_negative(arr, k):  
    result = []  
    negatives = deque()  
    for i in range(len(arr)):  
        if arr[i] < 0:  
            negatives.append(arr[i])  
        if i >= k:  
            if arr[i - k] < 0:  
                negatives.popleft()  
        result.append(negatives[0] if negatives else 0)  
    return result[k-1:]  