# 1. Find maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# 2. Sum all numbers in a list
def sum_list(numbers):
    return sum(numbers)

# 3. Reverse a string
def reverse_string(s):
    return s[::-1]

# 4. Factorial of a number
def factorial(n):
    if n < 0:
        return "Negative number does not have factorial"
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

# 5. Check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 6. Print prime numbers
def primes_less_than_n(n):
    return [x for x in range(2, n) if is_prime(x)]

def first_n_primes(N):
    primes = []
    num = 2
    while len(primes) < N:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# 7. Check perfect number
def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def perfect_numbers_less_than_1000():
    return [x for x in range(2, 1000) if is_perfect(x)]

# 8. Check pangram
import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())