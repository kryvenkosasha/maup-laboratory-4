def solve_cubic_equation(A, B, C, D):
    roots = set()

    for x in range(-100, 101):
        if A * x**3 + B * x**2 + C * x + D == 0:
            roots.add(x)

    return sorted(roots)


A, B, C, D = map(int, input("Введите коэффициенты A, B, C, D через пробел: ").split())


result = solve_cubic_equation(A, B, C, D)
print("Корни кубического уравнения в порядке возрастания:", *result)
