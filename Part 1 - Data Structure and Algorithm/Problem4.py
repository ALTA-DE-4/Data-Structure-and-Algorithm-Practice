def generate_primes_grid(width, height, start):
  result = []
  prime = start
  while len(result) < width * height:
    if is_prime(prime):
      result.append(prime)
    prime += 1
  return [result[i:i+width] for i in range(0, len(result), width)]

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True

print (generate_primes_grid(2, 3, 13))
print (generate_primes_grid(5, 2, 1))
