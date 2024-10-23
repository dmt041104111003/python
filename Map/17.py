def modify_string(s):  
    freq = Counter(s)  
    return ''.join(sorted(freq.keys(), key=lambda x: (-freq[x], x)))