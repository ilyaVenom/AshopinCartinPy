# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 07:55:19 2024
@author: segal
"""
# shopping cart game, to practice lists, sets and tuples:
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q": # makes Q -> q
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        # after these steps test it

# print decrative text:
print("++++ Your cart +++++") # and iterate over list
for food in foods:
    print(food, end=", ") # ends on the same line
    
# iterate the price:
for price in prices:
    total +=price

print(f"\n\nYour total comes to: $ {total}")




