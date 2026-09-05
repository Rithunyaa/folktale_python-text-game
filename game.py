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

print("~Kingdom Stats~")
print( f"   Treasury: {Treasury}")
print( f"   Military: {Military}")
print( f"   Food: {Food}")
print( f"   Reputation: {Reputation}")

situations = [
    {
        "person": "Farmer",
        "text": "ঌ All my crops burned down!! Please give me more food to feed my family! ঌ",
        "yes": {"food": -10, "reputation": 10},
        "no": {"food": 10, "reputation": -10}
    },

    {
        "person": "General",
        "text": "We need to train more soldiers! If we don't, we will be vulnerable to attack.",
        "yes": {"military": 10, "treasury": -10},
        "no": {"military": -10, "treasury": 10}
    }
]