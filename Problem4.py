#Problem4.py
#Name: Jaylen Atsou
#Date: March 8, 2026
#Assignment: Lab 7

# Problem 4
# Approach: multiply all 3-digit numbers by each other, check whether the product
# is a palindrome, and keep track of the largest palindrome found.
# Runtime note: checks many products, but retruns result almost instantly

from NumberTests import isPalindrome

def main():
  largest = 0

  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j

      if isPalindrome(product) and product > largest:
        largest = product

  print(largest)

if __name__ == '__main__':
  main()