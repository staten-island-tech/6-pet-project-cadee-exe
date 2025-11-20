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
    def __init__(self, name, money, inventory, food, happiness):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.happiness = happiness
        self.food = food
       
       
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def food(self, item):
        self.inventory.append(item)
        print(self.happiness)
   

        
rice = pet("atk", 150, ["Potion"],"food", "chasiu", "bao", "hunger")
print(rice.__dict__)

rice.buy("cannibalism")
print rice.dict
rice.food({"title":"happiness", "food": "chasiu", "bao", "hunger", "bar": 100 })

class pet:
    def __init__(self, name, atk):
        self.name = name
        self.atk = atk
    
    def display_info(self):
        return f"User: {self.name}, atk: {self.atk}"



