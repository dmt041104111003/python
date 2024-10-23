import heapq  

def closest_dorms(coords, k):  
    return heapq.nsmallest(k, coords, key=lambda x: x[0]**2 + x[1]**2)  