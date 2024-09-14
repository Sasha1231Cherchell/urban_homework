# Распаковка позиционных параметров

def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)


print_params()
print_params(1, 2, 3)
print_params("слонь", "конь", "морж")
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [9, True, "СЛОН"]
values_dict = {
    "a": 10,
    "b": 12.3,
    "c": False,
}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [6, "катя"]
print_params(*values_list_2, 42)