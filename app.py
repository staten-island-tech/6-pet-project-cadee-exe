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
    def __init__(self, name, inventory, feed, happiness, hunger, food, live):
        self.name = name
        self.inventory = inventory
        self.happiness = happiness
        self.food = food
        self.hunger = hunger
        self.feed = feed
        self.live = True
        
      
        self.happiness = 50
        self.hunger = 50

    def hungry(self):
         while self.live == True:
            if self.hunger >= 50 and self.hunger <= 100:
                print(f"{self.name} is not very hungry, hunger is at {self.hunger}")
                break
            elif self.hunger < 50:
                print(f"{self.name} is starving, hunger at {self.hunger}")
                break
            elif 


    def happy(self):
        while self.live == True:
            
            play = input("What would you like to do with fish?")
      

      

    

fish = pet("fish", ["fish"], "food", "happiness", "hunger", "feed", {"live= True"})

fish.__dict__()
fish.hunger()
fish.happiness()
    

