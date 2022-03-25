class Solution:
    def countPrimes(self, n: int) -> int:
        
        primes =[]
        
        is_prime =[False,False] + [True]*(n-1)
        
        for p in range(2,n):
            if is_prime[p]:
                primes.append(p)

                for i in range(p,n,p):
                    is_prime[i] =False
        return len(primes)
        