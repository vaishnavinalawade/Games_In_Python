def seive_of_eratosthenes_meth_1(n):
    limitn = n+1
    not_prime = [False]*limitn
    prime = []
    
    for i in range(2,limitn):
        if not_prime[i]:
            continue
        
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True
            
        prime.append(i)
    return prime

def prime_sieve_meth_2(limit):
    limitn = limit + 1
    not_prime = set()
    primes = []
    
    for i in range(2,limitn):
        if i in not_prime:
            continue
        
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        
        primes.append(i)
    print primes
    
def seive_of_eratosthenes_meth_3(n):
    prime = [True for i in range(n+1)]
    p = 2
    
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
        
    for p in range(2,n):
        if prime[p]:
            print p
 
 #Driver Program
if __name__=='__main__':
    n = 60
    print "Following are the prime numbers below ", n
    seive_of_eratosthenes_meth_1(n)
    prime_sieve_meth_2(n)
    seive_of_eratosthenes_meth_3(n)
    
    
