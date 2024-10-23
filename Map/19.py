def check_sum(arr, target):  
    seen = set()  
    return any((target - num) in seen or seen.add(num) for num in arr)