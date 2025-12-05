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
    def __init__(self, name, inventory, feed, happiness, hunger, food, live, play):
        self.name = name
        self.inventory = inventory
        self.happiness = happiness
        self.food = food
        self.hunger = hunger
        self.feed = feed
        self.live = live
        self.play = play
        live = True

      
        self.happiness = 50
        self.hunger = 50

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def activities(self, choice):
        while self.live == True:
            self.activities(choice = input("What would you like to do? play/feed/ignore"))
            if choice == "feed":
                self.feed(eat = input("what would you feed rice?"))
                stats = input("do you want stats rn? y/n")
                if stats == "y":
                    print(rice.__dict__)
                if self.live == True:
                    self.activities(input = ("what else would you like to do?"))
            elif stats == "n":
                self.activities(input("what else yould you like to do?"))
            if self.live == True:
                if choice == "play":
                    print(f"{self.name}'s happiness is at {self.happiness}")
                if stats == "ignore":
                    print(f"{self.name} is sad, please do something with bro")
                    self.happiness -=25


    def eat(self, nom):
       if nom in self.inventory:
             self.hunger += 10
             if self.hunger < 50:
                 print(f"{self.name} is starving, pls feed him. Hunger is at {self.hunger}")
             if self.hunger > 100:
                print(f"{self.name} is overfed, dont feed. hunger at {self.hunger}")
       else:   
             print(f"{self.name}'s hunger is at {self.hunger}")

    def fun(play, choice, self):
        while self.live == True:
                play == input("what would you like to do with rice?")
                if choice == "ap world history" or "job":
                    happiness -=10
                    print(f"whoops! shouldn't have done that! {self.name}'s happiness is at {self.happiness}") 
        else:
            print(f"{self.name} is happy! Happiness at {self.happiness}")


    def ignore(self, choice):
        while self.live == True:
            self.ignore(choice = input("do you want to ignore rice?"))
            if self.hunger < 15:
                self.live == False
            if self.happiness < 15:
                self.live == False
            if self.live == False:
                break
  

            
rice = pet("rice", ["rice"], ["cha siu", "bao", "burger", "apple", "cheeseburger", "sushi"], 
           "hunger", "happiness", "feed", "live= True", ["soccer", "catch", "job", "roblox", "video games", "ap world history"])
print(rice.__dict__)
  

    

