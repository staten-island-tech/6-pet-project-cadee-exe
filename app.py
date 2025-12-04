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

class pet:
    def __init__(self, name, inventory, feed, happiness, hunger, food, live):
        self.name = name
        self.inventory = inventory
        self.happiness = happiness
        self.food = food
        self.hunger = hunger
        self.feed = feed
        self.live = live
        live = True

      
        self.happiness = 50
        self.hunger = 50

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)


    def hungry(self):
            if self.hunger >= 50 and self.hunger <= 100:
                print(f"{self.name} is not very hungry, hunger is at {self.hunger}")
            elif self.hunger < 50:
                print(f"{self.name} is starving, hunger at {self.hunger}")
            else:
                print(f"{self.name} is too fat, {self.name} is gonna die")
            self.live = False

    def eat(self, food):
       notfood = ["bean", "cha siu", "apple", "burger", "glass", "homework", "bacon", "croissant", "baguette", "garlic", "baconetta", "usagi"]
       while self.live == True:
            if food in notfood:
                self.hunger += 5
                print(f"{self.name}'s hunger is now at {self.hunger}.")
            else:
                print(f"{self.name} doesn't own {self.food}.")
    eat("rice", "glass")

    def happy(self, activities):
       while self.live == True:
            play = input(f"What would you like to do with {self.name}?")
            activities == ["fetch", "job", "sewing", "exercise", "getting posessed", "video games", "tv", "addiction"]
rice = pet("rice", ["rice"], "food", "happiness", "hunger", "feed", ["live= True"])



    

