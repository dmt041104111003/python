def diversity(s, k):  
    unique_chars = len(set(s))  
    return max(0, k - unique_chars) if unique_chars <= k else "impossible"