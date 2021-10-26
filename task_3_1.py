# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b на квадраты с
# наибольшей возможной на каждом этапе стороной. Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

def quad(a, b, counter):
    if b == a:
        return a, counter + 1
    elif a < b:
        return quad(a, b - a, counter + 1)
    return quad(a - b, b, counter + 1)


a, b = int(input('Введите а: ')), int(input('Введите b: '))
counter = 0
result = quad(a, b, counter)
print(f'Длинна ребер: {result[0]}', f'\nКол-во полученных квадратов: {result[-1]}')