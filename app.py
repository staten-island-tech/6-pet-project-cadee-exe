# class Calculator():
#     def add(x, y):
#         print(x + y)
#         return x + y

# #     def add_many(numbers):
# #         print(sum(numbers))
# #         return sum(numbers)

# #     def subtract(numbers):
# #         return numbers

# # Calculator.add(767676, 888)

class pet:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)


rice = pet("Bread", 150, ["Potion"])

rice.buy({"title": "cha siu", "atk": 100})
print(rice.__dict__)

