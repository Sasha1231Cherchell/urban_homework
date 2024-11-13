import os.path


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'product.txt'

    def __init__(self):
        pass

    def get_products(self):
        if not os.path.exists(self.__file_name):
            return ""
        f = open(self.__file_name)
        data = f.read()
        f.close()
        return data

    def add(self, *products):
        data = self.get_products()
        f = open(self.__file_name, "a")
        for product in products:
            if str(product) in data:
                print(f"Продукт {product} уже есть в магазине")
            else:
                f.write(str(product) + "\n")
        f.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())



