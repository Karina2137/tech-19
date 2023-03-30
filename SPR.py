for i in range(10, 100):
  ilosc = 0
  ilosc += i % 10
  ilosc += i // 10
  a = ilosc
  b = i
  while b > 0:
    a, b = b, a%b
  if i//a > 1 and i//a < 10 and ilosc // a == 1:
    print(f"{ilosc}/{i}")