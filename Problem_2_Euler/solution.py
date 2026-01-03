def fib():
    a, b = 1, 2
    sum = 0
    while b <= 4_000_000:
        sum += b if b % 2 == 0 else 0
        a, b = b, a + b
    return sum
print(fib())