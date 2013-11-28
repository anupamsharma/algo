import math
import sys

def get_primes(n):
    """
    Returns a n+1 length boolean list a indicating if i is prime by value of a[i]. It usage Sieve of Eratosthenes for
    this.

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
