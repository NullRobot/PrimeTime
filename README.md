# Prime Time
PrimeCrafter is a command-line Python script designed to generate large prime numbers and factorize composite numbers. It is particularly useful for demonstrating the principles of public key cryptography, as it illustrates the challenge of factoring large numbers, a problem that ensures the security of cryptographic algorithms like RSA.

# Requirements:
- No requirements other than a Python interpreter (Python 3.x recommended)
  
# Usage:
To use PrimeCrafter, navigate to the directory containing the script and run it using the Python interpreter. There are two main modes of operation:

1. Generating Prime Numbers:
   To generate prime numbers of a specific length (number of digits), use the following command:
   ```
   python PrimeCrafter.py --generate <length>
   ```
   Replace `<length>` with the desired length of the prime numbers.

2. Factorizing Composite Numbers:
   To factorize a composite number and estimate the time it would take to do so, use the following command:
   ```
   python PrimeCrafter.py <composite_number>
   ```
   Replace `<composite_number>` with the composite number you wish to factorize.

# Features:
- Generate two large prime numbers of a specified length.
- Calculate the product of the two generated primes, which can be used as the modulus in RSA public key cryptography.
- Offer to factorize the generated composite number, providing an estimated and actual time for the factorization process.
- Factorize a user-provided composite number and estimate the time required for the process.

# Demonstration of Public Key Cryptography:
PrimeCrafter demonstrates public key cryptography by generating prime numbers that can serve as secret keys in the RSA algorithm. The product of these primes forms the public key modulus, which can be shared openly. The script emphasizes the difficulty of reversing this process (factoring the modulus) without the secret keys, thereby demonstrating the security provided by the RSA algorithm.

# Note:
The time estimation feature is a rough approximation and actual factorization times may vary based on the system's performance and the specific number being factorized.

