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
    def __init__(self, name, inventory, feed, happiness, hunger, food):
        self.name = name
        self.inventory = inventory
        self.happiness = happiness
        self.food = feed
        self.hunger = hunger
        self.feed = food
        
      
        self.happiness = 0
        self.hunger = 0

    
    def hungry(self, food):
         self.hunger.append(food)
         self.hunger += 5
         print(f"{self.name}'s hunger is at {self.hunger}")
         if self.hunger > 75:
            print("Rice is full. any more food and hes too fat")   
         if self.hunger < 75:
            print("Rice is too hungry hes gonna die")
         if self.hunger > 100:
             print("ur gonna kill rice bro hes fat")

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    

    def happy(self, item):
        self.happiness.append(item)
        self.happiness += 10
        print(f"{self.name}'s happiness is at {self.happiness}")
        if self.happiness > 50:
            print("rice is happy")
        if self.happiness < 50:
            print("rice is depressed")
        if self.happiness  > 100:
            print("rice is too jolly")

 
    eat = input("What would you like to feed rice?")
    def eats(food, hunger):
        hunger += 5
        print(f"You fed Rice a {food}, Hunger increased by, {hunger}")
        if food not in item:
            print("Uh oh: food no exist. sorry!")
        
   
            item = ["bean", "sushi", "cheeseburger", "baguette", "pear", "beans on toast", "job application", "tomato", "grape", "pizza", "chicken", "teriyaki", "salmon", "french fries"
                     "rice cake", "cake", "ice cream", "juice", "pibbl", "ruler",
                        "fetch", "cooking", "drawing", "reading", "rolling around", "being big", "job", "working", 
                          "school", "playing", "Roblox", "unemploynent", "money"]
        
rice = pet("rice", ["rice"], "food", "happiness", "hunger", "feed")
    

rice.buy("cannibalism")
rice.buy("cha siu")
rice.buy("bao")
print (rice.__dict__)

    

