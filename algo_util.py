import math
import sys

def get_primes(n):
    """
    Returns a n+1 length boolean list a indicating if i is prime by value of a[i]. It usage Sieve of Eratosthenes for
    this.
    doctest
    >>> get_primes(5)
    [True, True, True, True, False, True]

    """
    assert(n>1)
    primes = [True for i in range(0, n + 1)]
    m = math.floor(math.sqrt(n))
    count = 2
    while(count <= m):
        if primes[count]:
            m_in = n/count
            for i in range(2 * count, m_in * count + 1, count):
                primes[i] = False
        count = count + 1
    return primes
count = 0
print "prime Numbers"
for i in get_primes(28):
    if i: sys.stdout.write(str(count) + " ")
    count = count + 1
print "\nend" 

def gcd(a, b):
    """
    Calculates Greatest common devisor of two number using Euclid's theorem.
    >>> gcd(5,4)
    1
    
    >>> gcd(10,4)
    2
    
    >>> gcd(50,10)
    10
    
    >>> gcd(1, 20)
    1
    
    >>> gcd(20, 20)
    20
    
    """
    if (a==b):
        return a
        
    if (a==1 or b==1):
        return 1
    
    x1 = max(a,b)
    x2 = min(a,b)
    rem = x1 % x2
    if rem == 0:
        return x2
    else:
        return gcd(x2, rem)
