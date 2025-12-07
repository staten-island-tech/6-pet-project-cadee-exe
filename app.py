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
  

class pet:
    def __init__(dawg, name, happy, health, hunger):
        dawg.name = name
        dawg.hunger = hunger
        dawg.happy = happy
        dawg.health = health

    def play(dawg, happy, health, hunger):
        dawg.happy += happy
        dawg.health += health
        dawg.hunger -= hunger

    def feed(dawg, happy, health, hunger):
        dawg.happy += happy
        dawg.health += health
        dawg.hunger += hunger

    def ignore(dawg, happy, health, hunger):
        dawg.happy -= happy
        dawg.health -= health
        dawg.hunger -= hunger

    def shower(dawg, happy, health):
        dawg.happy -= happy
        dawg.health -= health

class YOU:
    def __init__(self, money, food):
        self.money = money
        self.food = food

    def buy(self, money, food):
        self.money -= money
        self.food += food

    def work(self, balance):
        self.money += balance

items = ["brick","coconut","Youtube sponsorship","poop","book","penny from the empire state building"]
activities = ["frisbee","Valorant","fetch","football","tug of war","hide and seek"]
foodlist = ["canned tuna","peanut butter","A5 wagyu","chicken","Dubai Chocolate, shouldn't have done that!","your homework"]
jobs = ["beg in the streets", "work at Mcdonalds","scam citizens","sell pet pics online","fight a dragon","try and find a job"]
import random
Overhap = False
Overfed = False
Overhelf = False
Underhap = False
Underfed = False
Underhelf = False
Day = 0
Shower = 0
Yname = input("What's your name?")
Pname = input("What is your pet's name?")
Mypet = pet(Pname, 50, 50, 50)
Me = YOU(10, 5)
print(f"Okay, your name is {Yname} and your pet's name is {Pname}!")

petlive = True

while petlive == True:

    action = input(f"What do you want to do with {Pname}? (play/feed/ignore)")

    game = random.choice(activities)
    food = random.choice(foodlist)
    item = random.choice(items)
    job = random.choice(jobs)
    Time = random.randint(1,6)
    Event = random.randint(1,12)
    salary = random.randint(2,8)
    dream = random.randint(1,2)
    foodspawn = random.randint(1,3)
    moneysteal = random.randint(1,5)

    if action.lower() == "play":
        print(f"you played {game} with {Pname}")
        Mypet.play(20, 12, 12)
        Shower += 1
    elif action.lower() == "feed" and Me.food >= 1:
        if food == "Dubai Chocolate, shouldn't have done that!" or food == "your homework":
            Mypet.health -= 15
        print(f"you fed {Pname} {food}")
        Mypet.feed(8, 20, 25)
        Me.food -= 1
    elif action.lower() == "feed" and Me.food <= 1:
        storetrip = input("You're out of food! Do you want to go to the store? (yes/no)")
        if storetrip.lower() == "yes":
            menu = input(f"You go to the store and the store sells A: 10 food $20, B: 5 food $12, and C: 2 food $6, what do you buy? Your balance is ${Me.money}. (A/B/C)")
            if menu.lower() == "a" and Me.money >= 20:
                Me.buy(20, 10)
                print("You bought 10 randomized foods!")
                if food == "Dubai Chocolate, shouldn't have done that!" or food == "your homework":
                    Mypet.health -= 15
                    print(f"you fed {Pname} {food}")
                    Mypet.feed(8, 20, 25)
                    Me.food -= 1
            elif menu.lower() == "a" and Me.money <= 20:
                print("ah, too bad you should go to work")
                job = input("do you want to go to work? (yes/no)")
                if job == "yes" and job != "try and find a job":
                    print(f"You went to {job} for {salary} hours and got paid {salary*1.5} dollars! {Pname} was ignored for {salary} hours though...")
                    Me.money += salary*1.5
                    Mypet.ignore(4*(Time-1), 4*(Time-1), 4*(Time-1))
                elif job.lower() == "yes" and job == "try and find a job":
                    print(f"You tried to find a job but spent the whole day with no luck, ignoring {Pname} for {salary} hours")
                    Mypet.ignore(4*(Time-1), 4*(Time-1), 4*(Time-1))
                elif job.lower() == "no":
                    print(f"You wasted the whole day away, ignoring {Pname} for {Time} hours. Stubborn you!")
                    Mypet.ignore(8*(Time-1), 8*(Time-1), 8*(Time-1))


            if menu.lower() == "b" and Me.money >= 12:
                Me.buy(12,5)
                print("You bought 5 randomized foods!")
                if food == "Dubai Chocolate, shouldn't have done that!" or food == "your homework":
                    Mypet.health -= 15
                    print(f"you fed {Pname} {food}")
                    Mypet.feed(8, 20, 25)
                    Me.food -= 1
            elif menu.lower() == "b" and Me.money <= 12:
                print("ah, too bad you should go to work")
                job = input("do you want to go to work? (yes/no)")
                if job.lower() == "yes" and job != "try and find a job":
                    print(f"You went to {job} for {salary} hours and got paid {salary*1.5} dollars! {Pname} was ignored for {salary} hours though...")
                    Me.money += salary*1.5
                    Mypet.ignore(4*(Time-1), 4*(Time-1), 4*(Time-1))
                elif job.lower() == "yes" and job == "try and find a job":
                    print(f"You tried to find a job but spent the whole day with no luck, ignoring {Pname} for {salary} hours")
                    Mypet.ignore(4*(Time-1), 4*(Time-1), 4*(Time-1))
                elif job.lower() == "no":
                    print(f"You wasted the whole day away, ignoring {Pname} for {Time} hours. Stubborn you!")
                    Mypet.ignore(8*(Time-1), 8*(Time-1), 8*(Time-1))


                if menu.lower() == "c" and Me.money >= 6:
                    Me.buy(5,2)
                    print("You bought 2 randomized foods!")
                    if food == "Dubai Chocolate, shouldn't have done that!" or food == "your homework":
                        Mypet.health -= 15
                        print(f"you fed {Pname} {food}")
                        Mypet.feed(8, 20, 25)
                        Me.food -= 1
                elif menu.lower() == "c" and Me.money <= 6:
                    print("ah, too bad you should go to work")
                    job = input("do you want to go to work? (yes/no)")
                    if job.lower() == "yes" and job != "try and find a job":
                        print(f"You went to {job} for {salary} hours and got paid {salary*1.5} dollars! {Pname} was ignored for {salary} hours though...")
                        Me.money += salary*1.5
                        Mypet.ignore(4*(Time-1), 4*(Time-1), 4*(Time-1))
                    elif job.lower() == "yes" and job == "try and find a job":
                        print(f"You tried to find a job but spent the whole day with no luck, ignoring {Pname} for {salary} hours")
                        Mypet.ignore(4*(Time-1), 4*(Time-1), 4*(Time-1))
                    elif job.lower() == "no":
                        print(f"You wasted the whole day away, ignoring {Pname} for {Time} hours. Stubborn you!")
                        Mypet.ignore(8*(Time-1), 8*(Time-1), 8*(Time-1))
                
        elif storetrip.lower() == "no":
            print(f"You wasted the whole day away, ignoring {Pname} for {Time} hours. Stubborn you!")
            Mypet.ignore(8*(Time-1), 8*(Time-1), 8*(Time-1))


    elif action.lower() == "ignore":
        print(f"you ignored {Pname} for {Time} hours, how cruel!")
        Mypet.ignore(8*(Time-1), 8*(Time-1), 8*(Time-1))
    else:
        print(f"Invalid activity, what do you want to do with {Pname}")
        Day -= 1

        if Event == 1:
            print(f"While chilling, a {item} fell on {Pname}'s head!")
            if item in ["brick", "coconut", "Youtube sponsorship"]:
                Mypet.health -= 20
                Mypet.happy -= 10
            else:
                Mypet.health -=10
                Mypet.happy -= 20
        if Shower >= 3:
            showerin = input(f"{Pname} is very dirty! Do we clean him? (yes/no)")
            if showerin.lower() == "no":
                Shower = 3
                print(f"{Pname} is now stinky!")
            elif showerin.lower() == "yes":
                print(f"You scrubbed {Pname} until he was shining, he's now very clean!")
                Shower = 0
            if Shower >= 3:
                Mypet.shower(8,8)

    if Mypet.hunger >= 70:
        print(f"{Mypet.name} is very full")
    elif Mypet.hunger >=50 and Mypet.hunger < 70:
        print(f"{Mypet.name} is full")
    elif Mypet.hunger <=25:
        print(f"{Mypet.name} is very hungry")
    elif Mypet.hunger <50 and Mypet.hunger > 25:
        print(f"{Mypet.name} is hungry")
    if Mypet.happy >= 70:
        print(f"{Mypet.name} is very happy")
    elif Mypet.happy >=50 and Mypet.happy < 70:
        print(f"{Mypet.name} is happy")
    elif Mypet.happy <=25:
        print(f"{Mypet.name} is very sad")
    elif Mypet.happy <50 and Mypet.happy > 25:
        print(f"{Mypet.name} is sad")
    if Mypet.health >= 70:
        print(f"{Mypet.name} is very healthy")
    elif Mypet.health >=50 and Mypet.health < 70:
        print(f"{Mypet.name} is healthy")
    elif Mypet.health <=25:
        print(f"{Mypet.name} is very unhealthy")
    elif Mypet.health <50 and Mypet.health > 25:
        print(f"{Mypet.name} is unhealthy")
    print(f"You have {Me.food} food items left and you have ${Me.money} left.")

    if Mypet.happy > 100:
        Overhap = True
    if Mypet.hunger > 100:
        Overfed = True
    if Mypet.health > 100:
        Overhelf = True
    if Mypet.happy < 1:
        Underhap = True
    if Mypet.hunger < 1:
        Underfed = True
    if Mypet.health < 1:
        Underhelf = True

    if Overhap == True:
        print(f"{Pname} passed away, he was too happy")
    if Underhap == True:
        print(f"{Pname} passed away, he was too sad")
    if Overfed == True:
        print(f"{Pname} passed away, he was too fat")
    if Underfed == True:
        print(f"{Pname} passed away, he was too hungry")
    if Overhelf == True:
        print(f"{Pname} passed away, he was too healthy")
    if Underhelf == True:
        print(f"{Pname} passed away, he was too unhealthy")

    nightact = input("It's late now, do you want to go to sleep, or get some work done for a little extra change? (sleep/work)")
    if nightact.lower() == "sleep" and dream == 1:
        print(f"You had a good dream and when you woke up, there was {foodspawn} pet food by your pillow!")
        Me.food += foodspawn
    elif nightact.lower() == "sleep" and dream == 2 and Me.money >= moneysteal:
        print(f"You had a horrible nightmare and when you woke up, your wallet was missing {moneysteal} dollars...")
    elif nightact.lower() == "sleep" and dream == 2 and Me.money < moneysteal:
        print(f"You had a horrible nightmare and found that your wallet had no money...")
        Me.money = 0
    elif nightact.lower() == "yes" and job != "try and find a job":
        print(f"You went to {job} for {salary} hours and got paid {salary} dollars!")
        Me.money += salary
    elif nightact.lower() == "yes" and job == "try and find a job":
        print("You tried to find a job during the night time but with no luck...")

    Day += 1
    print(f"It's day {Day}!")

    if Overhap or Underhap or Overfed or Underfed or Overhelf or Underhelf:
        print(f"You let {Pname} die after {Day} days! {Yname}, you absolute MONSTER! GAME OVERR!!")
        petlive = False
    if petlive == False:
        break


