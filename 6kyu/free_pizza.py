# https://www.codewars.com/kata/595910299197d929a10005ae

def pizza_rewards(customers, min_orders, min_price):
    return_customers = []
    
    for customer, orders in customers.items():
        count_price = sum(1 for order in orders if order >= min_price)
        
        if count_price >= min_orders:
            return_customers.append(customer)
    
    return return_customers

min_orders = 5
min_price = 20
customers = {
        'John Doe' : [22, 30, 11, 17, 15, 52, 27, 12], # Only has four orders of 20$ or more, so no pizza
        'Jane Doe' : [5, 17, 30, 33, 40, 22, 26, 10, 11, 45] # Has six orders of 20$ or more, which means FREE PIZZA!
        }
print(pizza_rewards(customers, min_orders, min_price))