"""
Shipping Prices
Shelley Wilson
1-26-22

Program that asks user for weight of package.
Takes in the price per pound based on weight entered.
Gives total cost for each method of shipping.
"""

weight = float(input("Enter weight of package: "))
#Ground Shipping
if weight <= 2:
  cost = 1.50
elif weight <= 6:
  cost = 3.00
elif weight <= 10:
  cost = 4.00
elif weight >= 10.01:
  cost = 4.75
else:
  print("Enter an accurate weight in pounds.")

ground_shipping = weight * cost + 20.00
print("Ground Shipping Price: $" + str(ground_shipping))
ground_premium = weight * cost + 125.00
print("Premium Ground Shipping Price: $" + str(ground_premium))

#Drone Shipping
if weight <= 2:
  drone_cost = 4.50
elif weight <= 6:
  drone_cost = 9.00
elif weight <= 10:
  drone_cost = 12.00
elif weight >= 10.01:
  drone_cost = 14.25
else:
  print("Please enter an accurate weight in pounds.")

drone_shipping = weight * drone_cost
print("Drone Shipping Price: $" + str(drone_shipping))


