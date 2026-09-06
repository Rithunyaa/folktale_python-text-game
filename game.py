#stats that you start with
Treasury = 100
Military = 50
Food = 50
Reputation = 100

#game title, the first few things that show up that tell you what is happening
print("        ✦ •······················• ✦ •······················• ✦")
print("                    Your Majesty, We Have A Problem")
print("        ✦ •······················• ✦ •······················• ✦")
print()
print("Your goal is to keep the kingdom running for as long as possible!")
print("To do this, you'll have to manage four stats. If any of these stats reach 0 ... game over.")
print()

print("~Initial Kingdom Stats~")
print( f"   Treasury: {Treasury}")
print( f"   Military: {Military}")
print( f"   Food: {Food}")
print( f"   Reputation: {Reputation}")
print()

input("Press ENTER to begin your day...")

situations = [
    {
        "person": "Farmer",
        "text": "ঌ All my crops burned down!! Please give me more food to feed my family! ঌ",
        "yes": {"food": -10, "reputation": 10},
        "no": {"food": 10, "reputation": -10}
    },

    {
        "person": "General",
        "text": "⚔︎ We need to train more soldiers! If we don't, we will be vulnerable to attack. ⚔︎",
        "yes": {"military": 10, "treasury": -10},
        "no": {"military": -10, "treasury": 10}
    }
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

    if choice == "yes":
        changes = situation["yes"]

    elif choice == "yes":
        changes = situation["no"]

    else:
        print("Please enter either YES or NO!")
        continue
    
print()
print("Results")
print("---------")

for stat, amount in changes.items():

    if stat == "treasury":
        treasury += amount

    elif stat == "military":
        military += amount

    elif stat == "food":
        food += amount

    elif stat == "reputation":
        reputation += amount

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
        print("You have run out of money.")
        print("The kingdom can no longer afford to function.")
        break

    elif Military <= 0:
        print("━─━────༺༻────━─━")
        print("     FAILURE")
        print("━─━────༺༻────━─━")
        print("Your military has completely collapsed.")
        print("The kingdom is left defenseless.")
        break

    elif Food <= 0:
        print("━─━────༺༻────━─━")
        print("     FAILURE")
        print("━─━────༺༻────━─━")
        print("The kingdom has run out of food.")
        print("Your people cannot survive.")
        break

    elif Reputation <= 0:
        print("━─━────༺༻────━─━")
        print("     FAILURE")
        print("━─━────༺༻────━─━")
        print("You have lost the people's trust.")
        print("Your reign has come to an end.")
        break

if (
    len(situations) == 0
    and treasury > 0
    and military > 0
    and food > 0
    and reputation > 0
):
    print()
    print("∘₊✧──────✧₊∘∘₊✧──────✧₊∘")
    print("        Day Over")
    print("∘₊✧──────✧₊∘∘₊✧──────✧₊∘")
    print()
    print("The day is finally over!")
    print("Another day having passed without")
    print("the kingdom falling apart.")
    print()
    print("Final Kingdom Stats:")
    print(f"Treasury:    {treasury}")
    print(f"Military:    {military}")
    print(f"Food:        {food}")
    print(f"Reputation:  {reputation}")