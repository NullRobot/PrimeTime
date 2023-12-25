import sys
import time
import math
from random import randrange

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(length):
    lower_bound = 10**(length - 1)
    upper_bound = (10**length) - 1
    while True:
        candidate = randrange(lower_bound, upper_bound)
        if is_prime(candidate):
            return candidate

def estimate_time(n):
    start_time = time.time()
    prime_factors(100000)
    end_time = time.time()
    time_for_small_number = end_time - start_time
    ratio = math.sqrt(n / 100000)
    estimated_time_seconds = time_for_small_number * ratio
    return estimated_time_seconds

def format_time(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365
    return (f"{seconds:.2f} seconds, "
            f"{minutes:.2f} minutes, "
            f"{hours:.2f} hours, "
            f"{days:.2f} days, "
            f"{years:.2f} years")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python PrimeMaster.py <composite_number> or python PrimeMaster.py --generate <length>")
        sys.exit(1)
    
    if sys.argv[1] in ["--generate", "-g"]:
        if len(sys.argv) != 3:
            print("Please specify the length of the prime numbers to generate.")
            sys.exit(1)
        try:
            length = int(sys.argv[2])
            if length <= 0:
                print("Length must be a positive integer.")
                sys.exit(1)
            prime1 = generate_prime(length)
            prime2 = generate_prime(length)
            product = prime1 * prime2
            print(f"Generated two prime numbers of length {length}: {prime1} and {prime2}")
            print(f"The product of the two primes is: {product}")
            print("This product can be used as the modulus in RSA public key cryptography. "
                  "The two primes are the secret keys and their product is used as part of the public key "
                  "which can be shared openly. The difficulty of factoring the product into its original primes "
                  "is what ensures the security of the RSA algorithm.")
            
            response = input("Do you want to factorize the composite number? (yes/no): ")
            if response.lower() in ["yes", "y"]:
                estimated_time_seconds = estimate_time(product)
                print("Estimated time for factorization:")
                print(format_time(estimated_time_seconds))
                
                start_time = time.time()
                factors = prime_factors(product)
                end_time = time.time()
                actual_time_taken = end_time - start_time
                
                print(f"The prime factors of {product} are: {factors}")
                print(f"Actual time taken for factorization: {actual_time_taken:.2f} seconds")
        except ValueError:
            print("Please enter a valid integer for the length.")
            sys.exit(1)
    else:
        try:
            composite_number = int(sys.argv[1])
            if composite_number <= 1:
                print("The number must be a composite number greater than 1.")
                sys.exit(1)
            
            estimated_time_seconds = estimate_time(composite_number)
            print("Estimated time for factorization:")
            print(format_time(estimated_time_seconds))
            
            start_time = time.time()
            factors = prime_factors(composite_number)
            end_time = time.time()
            actual_time_taken = end_time - start_time
            
            print(f"The prime factors of {composite_number} are: {factors}")
            print(f"Actual time taken for factorization: {actual_time_taken:.2f} seconds")
        
        except ValueError:
            print("Please enter a valid integer.")
            sys.exit(1)
