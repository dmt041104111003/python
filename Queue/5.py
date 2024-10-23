def is_prime(num):  
    if num < 2:  
        return False  
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:  
            return False  
    return True  

def super_prime_number(n):  
    super_primes = []  
    for num in range(2, n + 1):  
        if is_prime(num):  
            temp = num  
            while temp > 0:  
                if not is_prime(temp):  
                    break  
                temp //= 10  
            else:  
                super_primes.append(num)  
    return super_primes  