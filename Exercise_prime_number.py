n = 100

for i in range(2, n):
    d = 2
    isPrime = True

    while d <= i / 2:
        if i % d == 0:
            isPrime = False
            break
        d += 1

    if isPrime:
        print(f"{i} is a prime number")