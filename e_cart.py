class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # Appending item
        self.items.append(item)

    def remove_item(self, n):
        i = 0
        r = None
        for item in self.items:
            if item.name == n:
                r = i
            i += 1

        self.items.pop(r)

    def get_total_price(self):
        tp = 0
        for item in self.items:
            tp += item.price

        dis_price = 0

        if 5 <= len(self.items) < 10:
            dis_price = (tp * 15) / 100

        if 10 < len(self.items) < 15:
            dis_price = (tp * 27) / 100

        if len(self.items) >= 15:
            dis_price = (tp * 45) / 100

        print(f"Bill")

        for item in self.items:
            print(f"{item.name}----{item.price}")
        print(f"total_price----{tp}")
        print(f"discounted total_price----{tp - dis_price}")

        return tp - dis_price


cart = Cart()

item_one = Item("Soap", 10)
item_two = Item("Gell", 20)
item_three = Item("Watch", 100)
item_four = Item("Phone", 200)
item_five = Item("Belt", 75)
item_six = Item("Water Bottle", 1000)

cart.add_item(item_one)
cart.add_item(item_two)
cart.add_item(item_three)
cart.add_item(item_four)
cart.add_item(item_five)
cart.add_item(item_six)

cart.remove_item("Phone")

total_amount = cart.get_total_price()

print(total_amount)
