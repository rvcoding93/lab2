# Program Name: Lab2.py
# Course: IT1114/Section W03
# Student Name: Ronnie Vincenty
# Assignment Number: Lab 2
# Due Date: 01/26/2025
# Purpose: This program calculates the total food cost for the KSU CCSE hackathon.
#          It computes the number of whole pizzas needed, their cost, the salad cost,
#          applies applicable discounts, calculates the delivery fee, and displays
#          the final amount due.
# Resources Used: No external sources were used. Only personal knowledge and course materials.

# Constants
pizza_cost = 15.99  # whole pizza cost
salad_cost = 7.99   # salad cost
slices_per_pizza = 12  # slices in a whole pizza
slices_per_person = 3  # slices per person
pizza_discount_threshold = 10  # discount if more than 10 whole pizzas are ordered
salad_discount_threshold = 10  # discount if more than 10 salads are ordered
discount_rate = 0.15  # discount rate
delivery_rate = 0.07  # delivery charge
min_delivery_fee = 20.00  # Minimum delivery charge

# Gather input from user
pizza_ord = int(input("Number of pizza orders: "))
salad_ord = int(input("Number of salad orders: "))

# Calculate pizzas
total_slices = pizza_ord * slices_per_person
whole_pizza = (total_slices + slices_per_pizza - 1) // slices_per_pizza  # Ceiling division without imports
pizza_order_cost = whole_pizza * pizza_cost

# Calculate salad
salad_order_cost = salad_ord * salad_cost

# Calculate discount
pizza_discount = (pizza_order_cost * discount_rate) if whole_pizza > pizza_discount_threshold else 0
salad_discount = (salad_order_cost * discount_rate) if salad_ord > salad_discount_threshold else 0
total_discount = pizza_discount + salad_discount

# Calculate delivery fee
pre_discount = pizza_order_cost + salad_order_cost
delivery_fee = max(pre_discount * delivery_rate, min_delivery_fee)

# Calculate total amount
final_total = pre_discount - total_discount + delivery_fee

# Print receipt for user
print(f"Pizzas ordered: {whole_pizza}")
print(f"Pizza cost $ {pizza_order_cost}")
print(f"Salad cost $ {salad_order_cost}")
print(f"Total $ {pre_discount}")
print(f"Discount $ {total_discount}")
print(f"Delivery fee $ {delivery_fee}")
print(f"Final total $ {final_total}")
