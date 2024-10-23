from collections import Counter  

def frequency_count(arr):  
    return dict(sorted(Counter(arr).items()))