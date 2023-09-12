def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(N):
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            yield num
            count += 1
        num += 1


N = 5
prime_generator = generate_primes(N)
for prime in prime_generator:
    print(prime)
