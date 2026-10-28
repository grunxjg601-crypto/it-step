
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.quantity > 0:
            self.products.append(product)
            product.quantity -= 1
            print("Товар додано в кошик!")
        else:
            print("Товару немає в наявності!")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                product.quantity += 1
                print("Товар видалено!")
                return
        print("Товар не знайдено!")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        for product in self.products:
            print(product.name, "-", product.price, "грн")
        print("Загальна вартість:", self.total_price(), "грн")

product1 = Product("Футболка", 350, 5)
product2 = Product("Джинси", 800, 3)
product3 = Product("Кепка", 200, 0)

cart = Cart()

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.show_cart()

cart.remove_product("Футболка")
cart.show_cart()
