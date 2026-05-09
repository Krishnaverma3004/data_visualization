# Q3. Create a program that generates the first N prime numbers using a for loop and also calculates the sum and average of those prime numbers.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True 
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
def calculate_sum_and_average(primes):
    total_sum = sum(primes)
    average = total_sum / len(primes) if primes else 0
    return total_sum, average
# Main program
N = int(input("Enter the number of prime numbers to generate: "))
prime_numbers = generate_primes(N)
total_sum, average = calculate_sum_and_average(prime_numbers)
print(f"First {N} prime numbers: {prime_numbers}")
print(f"Sum of prime numbers: {total_sum}")
print(f"Average of prime numbers: {average:.2f}")
#--------------------- output:---------------------
# Enter the number of prime numbers to generate: 10
# First 10 prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Sum of prime numbers: 129
# Average of prime numbers: 12.90