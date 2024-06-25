import random
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def gen_prime():
    while True:
        p = random.randint(1 << 15, 1 << 16)
        if is_prime(p):
            return p

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def L(x, n):
    return (x - 1) // n

def generate():
    while True:
        p = gen_prime()
        q = gen_prime()
        if gcd(p * q, (p - 1) * (q - 1)) == 1:
            break
    n = p * q
    lamb = lcm(p - 1, q - 1)
    while True:
        g = random.randint(1, n ** 2)
        if gcd(L(g, n), n) == 1:
            break

    mu = pow(L(pow(g, lamb, n ** 2), n), -1, n)
    pub = (n, g)
    priv = (lamb, mu)
    return pub, priv

def encode(pub, m):
    n, g = pub
    r = random.randint(1, n)
    return pow(g, m, n ** 2) * pow(r, n, n ** 2) % (n ** 2)

def decode(priv, pub, c):
    n, _ = pub
    lamb, mu = priv
    return L(pow(c, lamb, n ** 2), n) * mu % n

class Voter:
    def __init__(self, pub):
        self.pub = pub

    def vote(self, idx, n):
        return [encode(pub, 0) if i != idx else encode(pub, 1) for i in range(n)]

class Tally:
    def __init__(self, pub):
        self.pub = pub

    def count(self, votes, n):
        res = [1 for _ in range(n)]
        for vote in votes:
            for i in range(n):
                res[i] *= vote[i]
                res[i] %= pub[0] ** 2
        return res

class Show:
    def __init__(self, pub, priv):
        self.pub = pub
        self.priv = priv

    def show(self, res):
        return [decode(priv, pub, r) for r in res]

if __name__ == '__main__':
    pub, priv = generate()
    n = 3
    m = 20
    voters = [Voter(pub) for _ in range(m)]
    tally = Tally(pub)
    show = Show(pub, priv)
    votes = [voter.vote(i % n, n) for i, voter in enumerate(voters)]
    res = tally.count(votes, n)
    print(show.show(res))

