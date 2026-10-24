import math
import random

def f(x):
    return x - math.cos(x)

def sgn(x):
    if x < 0: return -1
    if x > 0: return 1
    return 0

def generate_interval():
    # Ограничиваем число попыток поиска отрезка
    for i in range(1000):
        a = random.uniform(0, 1)
        b = random.uniform(0, 1)
        if a > b: a, b = b, a
        if f(a) * f(b) < 0: return a, b
    raise ValueError("Не удалось найти отрезок со сменой знака")


def delp(a, b, e):
    k = 0
    i = sgn(f(a))
    x = (a + b) * 0.5

    while b - a >= e:
        k += 1
        x = (a + b) * 0.5
        r = f(x)
        if r == 0: return x, k
        if sgn(r) * i != 1: b = x
        else: a = x
    return x, k


# Заданная точность
e = 1e-5

# Случайный начальный отрезок
a, b = generate_interval()

print(f"Начальный отрезок: [{a:.8f}; {b:.8f}]")
print(f"f(a) = {f(a):.8f}")
print(f"f(b) = {f(b):.8f}")

# Вычисление корня
x, k = delp(a, b, e)

print(f"\nПриближённый корень: {x:.10f}")
print(f"Значение функции: {f(x):.10f}")
print(f"Число итераций: {k}")
print(f"Заданная точность: {e}")