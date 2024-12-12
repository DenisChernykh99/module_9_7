import math


def is_prime(func):
    def wrapper(*args):
        result = func(*args)

        # Проверка, является ли число простым
        if result <= 1:
            print("Не является ни простым, ни составным")
        else:
            limit = int(math.sqrt(result)) + 1
            for i in range(2, limit):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
