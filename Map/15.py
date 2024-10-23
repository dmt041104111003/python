def most_frequent(arr):  
    count = Counter(arr)  
    max_freq = max(count.values())  
    return [num for num, freq in count.items() if freq == max_freq]