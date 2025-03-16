import numpy as np
import matplotlib.pyplot as plt

class Equation:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def parabola(self, x):
        return self.a * x**2 + self.b * x + self.c

    def derivative(self, x):
        return 2 * self.a * x + self.b

    def integral(self, x):
        return (self.a * x**3) / 3 + (self.b * x**2) / 2 + self.c * x + self.d

if __name__ == "__main__":
    # Введите коэффициенты
    a, b, c, d = map(float, input("Введите через пробел a b c d: ").split())

    eq = Equation(a, b, c, d)

    x = np.linspace(-10, 10, 500)

    # График параболы и производной
    plt.figure(figsize=(8, 6))
    plt.plot(x, eq.parabola(x), label="Парабола (f(x))")
    plt.plot(x, eq.derivative(x), label="Производная (f'(x))", linestyle="--")
    plt.title("График параболы и производной")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

    # График параболы и интеграла
    plt.figure(figsize=(8, 6))
    plt.plot(x, eq.parabola(x), label="Парабола (f(x))")
    plt.plot(x, eq.integral(x), label="Интеграл (F(x))", linestyle="--")
    plt.title("График параболы и интеграла")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()
