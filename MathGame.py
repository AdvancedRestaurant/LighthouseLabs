questions = [
    [1, 2],
    [3, 1],
    [22, 42]
]

initialScore = 0

for a, b in questions:
    response = int(input("What's the value of " + str(a) + " + " + str(b) + "?"))
    if response == a + b:
        print("Correct answer")
        initialScore += 1
    else:
        print("Incorrect")

if initialScore > len(questions) / 2:
    print("Your score was " + str(initialScore) + " out of " + str(len(questions)))
else:
    print("You got " + str(initialScore) + " out of " + str(len(questions)) + ". Better luck next time")
