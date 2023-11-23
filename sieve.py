def f(n):
    def sieve_of_eratosthenes(limit):
        limitn = limit+1
        primes = dict()
        not_primes = [False] * limitn
        for ind in range(2, limitn):
            if not_primes[ind] is False:
                primes[ind] = sum(1 for digit in str(ind) if int(digit) % 2 == 0)
                for multiple in range(ind*ind, limitn, ind):
                    not_primes[multiple] = True
        return primes

    primes = sieve_of_eratosthenes(n)
    max_even_digits = max(primes.values())
    return max(k for k, v in primes.items() if v == max_even_digits and k < n)
