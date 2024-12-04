def is_prime(func):
    def foo(*args):
        k = 0
        summa = func(*args)
        for i in range(2, summa // 2):
            if summa % i == 0:
                k = k + 1
        if k <= 0:
            print("Простое")
        else:
            print("Составное")
        return summa
    return foo


@is_prime
def sum_three(*nums):
    nums_sum = 0
    for i in nums:
        nums_sum += i
    return nums_sum


result = sum_three(2, 3, 6)
print(result)


