def multiples(num):
  ans = 0
  for x in range(1, num):
      if (x % 3 == 0 or x % 5 == 0):
        ans += x
  return ans

print multiples(1000)