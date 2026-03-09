#Problem10.py
#Name: Jaylen Atsou
#Date: March 8, 2026
#Assignment: Lab 7

# Problem 10
# Find the sum of all primes below two million.
# Approach: loop through numbers below 2000000, use isPrime() from NumberTests,
# and add each prime to a running total.
# Runtime note: takes about 10 secs because many numbers are tested.



from NumberTests import isPrime

def main():
  total = 2

  for i in range(3, 2000000, 2):
    if isPrime(i):
      total += i

  print(total)

if __name__ == '__main__':
  main()