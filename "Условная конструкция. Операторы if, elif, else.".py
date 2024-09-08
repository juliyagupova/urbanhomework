first = int(input())
second = int(input())
third = int(input())

if first == second == third:
    print(3)  # Все три числа равны
elif first == second or first == third or second == third:
    print(2)  # Два числа равны
else:
    print(0)  # Нет равных чисел
