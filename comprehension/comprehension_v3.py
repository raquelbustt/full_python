generator1 = (i ** 2 for i in range(10) if i % 2 == 0)
generator = [i ** 2 for i in range(10) if i % 2 == 0]
print(next(generator1))
print(next(generator1))
print(generator) 