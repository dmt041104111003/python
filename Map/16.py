def count_char(s):  
    return sorted(f"{char} {count}" for char, count in Counter(s).items())