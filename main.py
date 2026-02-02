import random, time

#This program used to determine the success and failure rate of resolving "GMX Applied Experiment #55" with varrying numbers of GMX and Dinosaur monsters in your deck

'''
Card Effect:
Excavate the top cards of your Deck until you have excavated a “GMX” monster and a Dinosaur monster,
lose 400 LP for each excavated card,
then you can Fusion Summon 1 “GMX” Fusion Monster from your Extra Deck,
using any excavated monsters as material,
also shuffle the rest into the Deck.
You can only activate 1 “GMX Applied Experiment #55” per turn.
'''


def start():
    count = 0
    success = 0
    failure = 0
    while count < 100000:
        #alter the number of monsters in the deck by adding a 1 per GMX and a 2 per dinosaur (need to add an option later that counts for both dino/gmx monster)
        deck = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        excavate = list()
        LifePoints = 8000
        #loop will run as long as deck count or lifepoints are above zero, failure case is life points run out, success case is both monsters excavated before life points run out
        while len(deck) > 0:
            card = random.choice(deck)
            excavate.append(card)
            deck.remove(card)
            LifePoints -= 400
            if (1 in excavate and 2 in excavate):
                success += 1
                break
            elif LifePoints == 0:
                failure += 1
                break
        count += 1
        #print("Excavated: ", excavate)
        #print("Deck Size: ", len(deck))
        #print("Life Points: ", LifePoints)
    print("1 GMX, 1 Dinosaurs")
    print("Success: ", success / count * 100, "%")
    print("Failure: ", failure / count * 100, "%")

    #continued iterations on loops with more GMX and dino added
    count = 0
    success = 0
    failure = 0
    while count < 100000:
        deck = [1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        excavate = list()
        LifePoints = 8000
        while len(deck) > 0:
            card = random.choice(deck)
            excavate.append(card)
            deck.remove(card)
            LifePoints -= 400
            if (1 in excavate and 2 in excavate):
                success += 1
                break
            elif LifePoints == 0:
                failure += 1
                break
        count += 1
        #print("Excavated: ", excavate)
        #print("Deck Size: ", len(deck))
        #print("Life Points: ", LifePoints)
    print("3 GMX, 1 Dinosaurs")
    print("Success: ", success / count * 100, "%")
    print("Failure: ", failure / count * 100, "%")

    count = 0
    success = 0
    failure = 0
    while count < 100000:
        deck = [1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        excavate = list()
        LifePoints = 8000
        while len(deck) > 0:
            card = random.choice(deck)
            excavate.append(card)
            deck.remove(card)
            LifePoints -= 400
            if (1 in excavate and 2 in excavate):
                success += 1
                break
            elif LifePoints == 0:
                failure += 1
                break
        count += 1
        #print("Excavated: ", excavate)
        #print("Deck Size: ", len(deck))
        #print("Life Points: ", LifePoints)
    print("3 GMX, 3 Dinosaurs")
    print("Success: ", success / count * 100, "%")
    print("Failure: ", failure / count * 100, "%")

    count = 0
    success = 0
    failure = 0
    while count < 100000:
        deck = [1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        excavate = list()
        LifePoints = 8000
        while len(deck) > 0:
            card = random.choice(deck)
            excavate.append(card)
            deck.remove(card)
            LifePoints -= 400
            if (1 in excavate and 2 in excavate):
                success += 1
                break
            elif LifePoints == 0:
                failure += 1
                break
        count += 1
        #print("Excavated: ", excavate)
        #print("Deck Size: ", len(deck))
        #print("Life Points: ", LifePoints)
    print("6 GMX, 1 Dinosaurs")
    print("Success: ", success / count * 100, "%")
    print("Failure: ", failure / count * 100, "%")

    count = 0
    success = 0
    failure = 0
    while count < 100000:
        deck = [1, 1, 1, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        excavate = list()
        LifePoints = 8000
        while len(deck) > 0:
            card = random.choice(deck)
            excavate.append(card)
            deck.remove(card)
            LifePoints -= 400
            if (1 in excavate and 2 in excavate):
                success += 1
                break
            elif LifePoints == 0:
                failure += 1
                break
        count += 1
        #print("Excavated: ", excavate)
        #print("Deck Size: ", len(deck))
        #print("Life Points: ", LifePoints)
    print("6 GMX, 3 Dinosaurs")
    print("Success: ", success / count * 100, "%")
    print("Failure: ", failure / count * 100, "%")

    count = 0
    success = 0
    failure = 0
    while count < 100000:
        deck = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        excavate = list()
        LifePoints = 8000
        while len(deck) > 0:
            card = random.choice(deck)
            excavate.append(card)
            deck.remove(card)
            LifePoints -= 400
            if (1 in excavate and 2 in excavate):
                success += 1
                break
            elif LifePoints == 0:
                failure += 1
                break
        count += 1
        #print("Excavated: ", excavate)
        #print("Deck Size: ", len(deck))
        #print("Life Points: ", LifePoints)
    print("6 GMX, 6 Dinosaurs")
    print("Success: ", success / count * 100, "%")
    print("Failure: ", failure / count * 100, "%")


start()
