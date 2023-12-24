def solve_problem(N, numbers):
    positive_sum = sum([num for num in numbers if num > 0])
    
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)
    
    product = 1
    for i in range(start_index, end_index):
        product *= numbers[i]

    return positive_sum, product

# Пример входных данных
N = 10
numbers = [3, -4, 2, 7, 9, -5, 1, 8, -6, 10]

# Получение результата
result = solve_problem(N, numbers)

# Вывод результатов
print(f"Сумма положительных элементов: {result[0]}")
print(f"Произведение чисел между минимальным и максимальным элементами: {result[1]}")
