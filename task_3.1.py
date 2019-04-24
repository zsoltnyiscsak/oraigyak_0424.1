n = 5000
primes = set(range(2, n+1))
p = 2
while p<=n:
    if p in primes :
        for k in range (p+p,n+1,p):
            primes.discard(k)
    p+=1
print(primes)