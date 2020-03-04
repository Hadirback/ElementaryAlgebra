import numpy as np
import itertools


def get_probability(options, count, p, q):
    coeff = (np.math.factorial(count) / (np.math.factorial(options) * np.math.factorial(count - options)))
    return coeff * pow(p, options) * pow(q, (count - options))


# Реализация метода Монте Карло для последовательных и независимых испытаний
k, n = 0, 1000
# случйные векторы
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1


print(k, n, k/n)

print('Вероятность через формулу Бернулли - {0}'.format(get_probability(2, 4, 0.5, 0.5)))
print('При больших значениях n вероятность рассчитаная методом Монте-Карло стремится к вероятности рассчитаной по формуле Бернулли')


for p in itertools.product("01234", repeat=2):
    print(''.join(p))
print('------------')
# размещения или перестановка
for p in itertools.permutations('012', 3):
    print(''.join(str(x) for x in p))
print('------------')
for p in itertools.combinations("01234", 2):
    print(''.join(p))
