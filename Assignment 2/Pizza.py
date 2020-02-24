size = 'large'
toppings = ['onions', 'broccoli', 'pepper', 'peas', 'squid', 'pastrami', 'yellow squash', 'salmon', 'pepperoni', 'cilantro', 'coriander', 'fried onions', 'prawns', 'tuna', 'green olives', 'anchovies', 'anchovies', 'corn']
total = 0
top_cost = 0
if size == 'small':
    total = 14
elif size == 'medium':
    total = 16
else:
    total = 18
for index in range(len(toppings)):
    top_cost = ((12 + index + len(toppings[index])) / 100) * total
    total = total + top_cost
for str in toppings:
    if 'bacon' in str or 'anchovies' in str:
        total = total * 1.1
        break
    else:
        total = total
print(total)