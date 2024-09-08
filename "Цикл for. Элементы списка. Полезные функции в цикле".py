numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и не простых чисел
primes = []
not_primes = []

for number in numbers:
    if number == 1:
        continue  # Пропускаем 1, так как оно не является простым или составным

    is_prime = True  # Предполагаем, что число простое

    # Проверка, делится ли число на что-то кроме себя и 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        primes += [number]
    else:
        not_primes += [number]

print("Primes:", primes)
print("Not Primes:", not_primes)
