def get_password(n):
    result = ""
    used = set()

    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result += str(i) + str(j)
                used.add(i)
                used.add(j)
    return result

n = int(input("Введите число от 3 до 20: "))
result = get_password(n)
print(f"Пароль для числа {n}: {result}")
