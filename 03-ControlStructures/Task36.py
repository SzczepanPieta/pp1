n = int(input("Enter the value of N: "))

count = 0
primes = []

number = 2

while count < n:
  is_prime = True

  for i in range(2, number):
    if number % i == 0:
      is_prime = False
      break

  if is_prime:
    primes.append(number)
    count += 1

  number += 1

print("The first", n, "prime numbers are:", primes)
