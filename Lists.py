# list exercise. Given foosballers list
foosballers = [
    "Mia",
    "Retta",
    "Augustine",
    "Jin",
    "Waylon",
    "Alphonso",
    "Sage",
    "Hubert",
    "Raymon",
    "Rebecca",
    "Monty",
    "Glen",
    "Christi",
    "Patrice",
    "Craig",
    "Dexter",
    "Wally",
    "Ian",
    "Pat"
]

# getting the median player
people = len(foosballers)
medPosition = int(people / 2)
medPlayer = (foosballers[medPosition])
print(medPlayer)

# getting the 5 players in the middle of the league (2 above and 2 below the median player)
t5medPlayer = foosballers[medPosition - 2:medPosition + 3]

# inserting a fake player "Average player"
foosballers.insert(medPosition, "Average Player")

# replaing text of newly insearted fake player
foosballers[9] = "AVERAGE PLAYER"

# 5 more players are unranked and join the league. Added to the bottom of the list
newPlayers = ['Mark', 'Bear', 'Walter', 'Yuki', 'Leelee']
foosballers.extend(newPlayers)

# finding position of fake player and removing from the list
index = foosballers.index("AVERAGE PLAYER")
del foosballers[index]

# New rank players join the league. Finding position of players
Lacy = foosballers.index("Hubert")
Omar = foosballers.index("Rebecca")

# Lacy is one spot ahead of Hubert
foosballers.insert(Lacy, "Lacy")

# Omar is one spot behind Rebecca
foosballers.insert(Omar + 2, "Omar")

# Otto is 8th best in the league
foosballers.insert(7, "Otto")

# Chauncey is 10 spots from the bottom of the league
foosballers.insert(-9, "Chauncey")


