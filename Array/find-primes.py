def findPrimes():
    primes[0] = primes[1] = False
    i = 2
    while i*i < MAX:
        if primes[i]:
            for j in range(i*i, MAX, i):
                if primes[j]:
                    spf[j] = i
                primes[j] = False
        i += 1

def findPrimeFactors(num):
    primeFactors = set()
    while num != 1:
        sp = spf[num]
        primeFactors.add(sp)
        num = num // sp

    return list(primeFactors)