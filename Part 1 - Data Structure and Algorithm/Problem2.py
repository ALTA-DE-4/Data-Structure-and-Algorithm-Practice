def primeX(x):
    primes = [2]
    num = 3
    while len(primes) < x:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
        num += 2
    return primes[x-1]

print(primeX(1))  
print(primeX(5))  
print(primeX(8))  
print(primeX(9))  
print(primeX(10)) 
