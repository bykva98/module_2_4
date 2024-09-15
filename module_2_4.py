numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    #print(i)
    if i == 1:
        continue
    for k in range(2, i-1):
        if i % k == 0:
            is_prime = False
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes)
print('Not Primes: ', not_primes)


#Primes: [2, 3, 5, 7, 11, 13]
#Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]


