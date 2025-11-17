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
    def __init__(self, name, money, inventory, food):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.food = food
       
       
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def food(self, item):
        

    
rice = pet("rice", 150, ["Potion"])
rice.buy("cannibalism")

print(rice.__dict__)




