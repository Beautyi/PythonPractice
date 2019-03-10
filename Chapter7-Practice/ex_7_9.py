#pastrami卖完了
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'sushi', 'crisp', 'pastrami']
print(sandwich_orders)
print("The pastrami is sold out.")
while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
print(sandwich_orders)
