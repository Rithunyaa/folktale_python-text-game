# stats that you start with

Treasury = 100
Military = 100
Food = 100
Reputation = 100


# game title, the first few things that show up that tell you what is happening

print("        ✦ •······················• ✦ •······················• ✦")
print("                    Your Majesty, We Have A Problem")
print("        ✦ •······················• ✦ •······················• ✦")
print()

print("Your goal is to keep the kingdom running for as long as possible!")
print("To do this, you'll have to manage four stats. If any of these stats reach 0 ... game over.")
print()

print("~Initial Kingdom Stats~")

print(f"   Treasury: {Treasury}")
print(f"   Military: {Military}")
print(f"   Food: {Food}")
print(f"   Reputation: {Reputation}")

print()

input("Press ENTER to begin your day!   ")


situations = [

    {
        "person": "Farmer",
        "text": "ঌ All my crops burned down!! Please give me more food to feed my family! ঌ",
        "yes": {"food": -10, "reputation": +15},
        "no": {"reputation": -25}
    },

    {
        "person": "General",
        "text": "⚔︎ We need to train more soldiers! If we don't, we will be vulnerable to attack. ⚔︎",
        "yes": {"military": +20, "treasury": -15},
        "no": {"military": -5, "reputation": -10}
    },

    {
        "person": "Merchant",
        "text": "☼ The kingdom's marketplace is becoming crowded! Should we build a larger market? ☼",
        "yes": {"treasury": -25, "reputation": +15},
        "no": {"treasury": -5, "reputation": -10, "food": -5}
    },
    {
        "person": "Villager",
        "text": "❀ Our village well has dried up! Please give us coin to build a new one! ❀",
        "yes": {"treasury": -20, "reputation": +15},
        "no": {"reputation": -20, "food": -5}
    },
    {
        "person": "Knight",
        "text": "⚔︎ Bandits have been spotted near the northern village! Should we send soldiers to deal with them? ⚔︎",
        "yes": {"military": -10, "reputation": +15},
        "no": {"reputation": -15, "treasury": -10}
    },
    {
        "person": "Royal Treasurer",
        "text": "₊˚⊹ The treasury is looking rather empty. Should we raise taxes? ⊹˚₊",
        "yes": {"treasury": +20, "reputation": -30},
        "no": {"reputation": +5}
    },
]


import random


while len(situations) > 0:

    situation = random.choice(situations)

    print()
    print("------------------------------")
    print(situation["person"])
    print(situation["text"])
    print("------------------------------")

    choice = input("YES or NO: ").strip().upper()

    if choice == "YES":
        changes = situation["yes"]

    elif choice == "NO":
        changes = situation["no"]

    else:
        print("Please enter either YES or NO!")
        continue


    print()
    print("Results")
    print("---------")


    for stat, amount in changes.items():

        if stat == "treasury":
            Treasury += amount

        elif stat == "military":
            Military += amount

        elif stat == "food":
            Food += amount

        elif stat == "reputation":
            Reputation += amount

        if amount > 0:
            print(f"{stat.capitalize()}: +{amount}")

        elif amount < 0:
            print(f"{stat.capitalize()}: {amount}")


    print()
    print("UPDATED KINGDOM STATS")
    print("------------------------")

    print(f"Treasury:    {Treasury}")
    print(f"Military:    {Military}")
    print(f"Food:        {Food}")
    print(f"Reputation:  {Reputation}")


    situations.remove(situation)

    print()


    if Treasury <= 0:
        print("━─━────༺༻────━─━")
        print("     FAILURE")
        print("━─━────༺༻────━─━")
        print("You have no more money left")
        print("The kingdom cannot pay back its debts anymore")
        break

    elif Military <= 0:
        print("━─━────༺༻────━─━")
        print("     FAILURE")
        print("━─━────༺༻────━─━")
        print("Your military has grown weak")
        print("You have been overrun by bandits")
        break

    elif Food <= 0:
        print("━─━────༺༻────━─━")
        print("     FAILURE")
        print("━─━────༺༻────━─━")
        print("The kingdom has run out of food")
        print("Your people are starving")
        break

    elif Reputation <= 0:
        print("━─━────༺༻────━─━")
        print("     FAILURE")
        print("━─━────༺༻────━─━")
        print("The people do not trust you anymore")
        print("They have revolted against you")
        break

    input("\nPress ENTER to continue   ")


if (
    len(situations) == 0
    and Treasury > 0
    and Military > 0
    and Food > 0
    and Reputation > 0
):

    print()

    print("∘₊✧──────✧₊∘∘₊✧──────✧₊∘")
    print("        Day Over")
    print("∘₊✧──────✧₊∘∘₊✧──────✧₊∘")

    print()

    print("Another day has passed without the kingdom falling apart!")
    print("         Thank you for playing this game!")

    print()

    print("Final Kingdom Stats:")
    print(f"Treasury:    {Treasury}")
    print(f"Military:    {Military}")
    print(f"Food:        {Food}")
    print(f"Reputation:  {Reputation}")