# """ # class Calculator():
# #     def add(x, y):
# #         print(x + y)
# #         return x + y

# # #     def add_many(numbers):
# # #         print(sum(numbers))
# # #         return sum(numbers)

# # #     def subtract(numbers):
# # #         return numbers

# # # Calculator.add(767676, 888) """

class You:
    def __init__(self):
        self.name = input("you take care of rice ok so what ur name")

class pet:
    def __init__(self, name, money, inventory, food, happiness, hunger):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.happiness = happiness
        self.food = food
        self.hunger = hunger
      
       
        self.happiness = 0
        self.hunger = 0
    
    def hungry(self, food):
         self.hunger.append(food)
         self.hunger +=5
    
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def happy(self, item):
        self.happiness.append(item)
        self.happiness += 10
        print(f"{self.name}'s happiness is at {self.happiness}")

        self.food = ["bean", "sushi", "cheeseburger", "baguette", "pear", "beans on toast", "job application", "tomato", "grape", "pizza", "chicken", "teriyaki", "salmon", "french fries"
                     "rice cake", "cake", "ice cream", "juice", "pibbl"]
        self.happiness = ["fetch", "cooking", "drawing", "reading", "rolling around", "being big", "job", "working", 
                          "school", "playing", "Roblox", "unemploynent", "money"]

rice = pet("rice", 150, ["rice"],"food", "happiness", "hunger")

rice.buy("cannibalism")
rice.buy("cha siu")
rice.buy("bao")
print (rice.__dict__)

    

