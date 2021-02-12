# Simple tax calculator

subtotal = float(input("What is your subtotal? "))
tax = float(0.25)
taxOwed = subtotal * tax
total = subtotal + taxOwed
print(taxOwed)
print(total)

# simple bill splitter

billTotal = float(input("Enter total bill amount: "))
tipPercent = float(input("Enter tip percentage: "))
people = float(input("Number of people"))
tipbill = billTotal * (tipPercent/100)
payperperson = (billTotal + tipbill) / people
print("Each person should pay: " + str(payperperson))
