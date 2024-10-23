def largest_element(arr):  
    freq = Counter(arr)  
    min_freq = min(freq.values())  
    return max(num for num, count in freq.items() if count == min_freq)