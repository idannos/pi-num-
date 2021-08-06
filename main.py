import matplotlib.pyplot as plt
import math


def prime(n):
    if n % 2 == 0:
        return False  # number is not prime
    iterations = int(math.sqrt(n)) + 1
    for i in range(3, iterations, 2):
        if n % i == 0:
            return False
    return True


num = 100000 # the program will run to this number
primes = []
difference_between_primes = []
x = []
y = []
prime_counter=0
for i in range(3, num, 1):
    x.append(i)
    y.append(prime_counter)
    if prime(i):
        prime_counter += 1


# plotting points as a scatter plot
plt.scatter(x, y, label="", color="green", marker="*", s=30)

plt.ylabel('difference between the last prime and the prine itself')
plt.xlabel('numbers')
plt.title('difference between sequential primes')
plt.legend()
plt.show()
