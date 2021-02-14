instructionSteps = [
    "turn left",
    "go straight for 2 blocks",
    'turn right',
    'keep going until you see the dog statue',
    'turn right',
    'turn right again',
    'park right on the sidewalk',
]

instructions = "First, "

for nextInstructions in instructionSteps:
    instructions = instructions + nextInstructions + ", then "

print(instructions + "You're there!")

instructionsStepsButScreemed = []

for nextInstructions in instructionSteps:
    upperInstruction = nextInstructions.upper()
    instructionsStepsButScreemed.append((upperInstruction))

print(instructionsStepsButScreemed)

actors = [
    'Nathan Fillion',
    'Gina torres',
    'Alan Tudyk',
    'Morena Baccarin',
    'Adam Baldwin',
    'Jewel Staite',
    'Sean Maher',
    'Summer Glau',
    'Ron Glass'
]

roles = [
    'Captain Malcolm Reynolds',
    'Zoe Washburn',
    'Hoban Washburn',
    'Inara Serra',
    'Jayne Cobb',
    'Kaylee Frye',
    'Dr. Simon Tam',
    'River Tam',
    'Derrial Book'
]
# first method
print('Featuring:\n=-=-=-=-=-=-=-=-=-=-=-=')
for index in range(0, len(actors)):
    print(actors[index] + " as " + roles[index])

# second method
actorRoles = [
    ['Nathan Fillion', 'Captain Malcolm Reynolds'],
    ['Gina Torres', 'Zeo Washburn'],
    ['Alan Tudyk', 'Hoban Washburn'],
    ['Morean Baccarin', 'Inara Serra'],
    ['Adam Baldwin', 'Jayne Cobb'],
    ['Jewel Staite', 'Kaylee Frye'],
    ['Sean Maher', 'Dr. Simon Tam'],
    ['Summer Glau', 'River Tam'],
    ['Ron Glass', 'Derrial Book']
]

print('Featuring:\n=-=-=-=-=-=-=-=-=-=-=-=')
for actorRole in actorRoles:
    actor = actorRole[0]
    role = actorRole[1]
    print(actor + " as " + role)


