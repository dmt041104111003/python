def can_complete_circuit(gas, cost):  
    total, current, start = 0, 0, 0  
    for i in range(len(gas)):  
        total += gas[i] - cost[i]  
        current += gas[i] - cost[i]  
        if current < 0:  
            start = i + 1  
            current = 0  
    return start if total >= 0 else -1  