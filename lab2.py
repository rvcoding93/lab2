# Program Name: Lab2.py
# Course: IT1114/Section  W03
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

#gather input from user to pass through later
pizza_ord = int(input("Number of pizza orders: "))
salad_ord = int(input("Number of pizza orders: "))

#calculate pizzas
total_slices = pizza_ord * slices_per_person
whole_pizza = -(-total_slices//slices_per_pizza)
pizza_cost = whole_pizza * pizza_cost

#calculate salad
salad_cost = salad_ord * salad_cost

#calculate discount
pizza_discount = (pizza_cost * discount_rate) if pizza_ord > pizza_discount_threshold else 0
salad_discount = (salad_cost * discount_rate) if salad_ord > salad_discount_threshold else 0
toal_discount = pizza_discount + salad_discount

#delivery fee
pre_discount = pizza_cost + salad_cost
delivery_fee = max(pre_discount *  delivery_rate, min_delivery_fee)

#total amount
final_total = pre_discount - toal_discount + delivery_rate


#print receipt for user
print(f"pizzas ordered: {pizza_ord}")
print(f"pizza cost $ {pizza_cost}")
print(f"salad cost $ {salad_cost}")
print(f"discount $ {toal_discount}")
print(f"delivery fee $ {delivery_fee}")
print(f"final total $ {final_total}")


