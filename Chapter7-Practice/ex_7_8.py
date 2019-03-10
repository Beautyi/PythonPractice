#熟食店
sandwich_orders = ['tuna', 'sushi', 'crisp']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
