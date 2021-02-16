# Right almond milk
cartons = [
    ["Not almond milk", "Wrong logo"],
    ['Not almond milk', 'Wrong logo'],
    ['Almond milk', "Wrong logo"],
    ['Almond milk', 'Right logo'],
    ['Almond milk', 'Wrong logo'],
    ['Almond milk', 'Wrong logo']
]

cart = []

wrongCartonsLookedAt = 0

for carton in cartons:
    typeOfMilk = carton[0]
    logo = carton[1]
    if typeOfMilk is "Almond milk" and logo is "Right logo":
        cart.append(carton)
        break
    else:
        wrongCartonsLookedAt += 1

if len(cart) is 0:
    cart.append("Beer")

print(
    "I looked at " + str(wrongCartonsLookedAt) +
    " cartons that were not almond-painted-like-a-cow brand almond milk.")

# Can you ride a roller coaster?
age = 16

print("Can you ride this roller coaster?")
if age > 18:
    print("Definitely!")
elif age > 12:
    print("Maybe, How tall are you?")
else:
    print("Sorry, kid. Come back when you're older")

# Password checker
correctPassword = "shepard123"
enteredPassword = input("What's the password?")

if correctPassword == enteredPassword:
    print("Yeah! This is the correct password")
else:
    print("Wrong password")

# Password Validator
password = input("What password would you like to use?")
passwordConfirm = input("Please enter the password again")

if passwordConfirm != password:
    print("Both passwords need to match")
elif len(password) < 8:
    print("Chosen password is too short")
else:
    print("Password set")

