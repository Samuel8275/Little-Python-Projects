food_amount = int(input("What is the food amount? "))
tip_percentage = input("What is the tip percentage? ")
tip_percentage1 = int(tip_percentage) / 100
tip_amount = food_amount * tip_percentage1

total = food_amount + tip_amount

print("You have to pay: $" + str(total) )