def second_smallest(arr):  
    return sorted(set(arr))[1] if len(set(arr)) > 1 else "NO"