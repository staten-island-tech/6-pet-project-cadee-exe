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

    def happiness(self, item):
        self.happiness.append(item)
        self.happiness += 10
  
        print(f"{self.name}'s happiness is at {self.happiness}")
     
    def food(self, item):
        self.hunger += 25
        if self. food in item:
            print(f"{self.name}'s hunger is at {self.hunger}")
        if self.food not in item:
            print("rice is starving. Hp -1")
    
        self.food == item("no food")
        print(rice.__dict__)

        
rice = pet("atk", 150, ["Potion"],"food", "happiness")

rice.buy("cannibalism")
rice.buy("cha siu")
rice.buy("bao")
print (rice.__dict__)

class pet:
    def __init__(self, name, atk):
        self.name = name
        self.atk = atk
    
def display_info(self):
    return f"User: {self.name}, atk: {self.atk}"



