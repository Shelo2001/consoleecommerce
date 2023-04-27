from collections import defaultdict

# in-memory database
products = defaultdict(lambda: {'name': None, 'price': None, 'quantity': 0, 'purchases': []})
orders_history = {}

# command functions
def save_product(product_id, name, price):
    products[product_id]['name'] = name
    products[product_id]['price'] = float(price)


def purchase_product(product_id, quantity, price):
    products[product_id]['quantity'] += int(quantity)
    products[product_id]['purchases'].append(float(price))


def order_product(product_id, quantity):
    if product_id in orders_history:
        orders_history[product_id] += quantity
    else:

        orders_history[product_id] = quantity
    if products[product_id]['quantity'] < int(quantity):
        print(f"Insufficient stock for product {product_id}")
    else:
        products[product_id]['quantity'] -= int(quantity)


def get_quantity_of_product(product_id):
    print(products[product_id]['quantity'])


def get_average_price(product_id):
    purchases = products[product_id]['purchases']
    if not purchases:
        print("No purchase history for this product")
    else:
        avg_price = sum(purchases) / len(purchases)
        print(round(avg_price, 2))
print(products)

def get_product_profit(product_id):
    purchases = products[product_id]['purchases']
    if not purchases:
        print("No purchase history for this product")
    else:
        purchase_avg = sum(purchases) / len(purchases)
        orders = [o for o in orders_history if o['product_id'] == product_id]
        if not orders:
            print("No order history for this product")
        else:
            order_avg = sum([o['price'] for o in orders]) / len(orders)
            profit = order_avg - purchase_avg
            total_profit = profit * products[product_id]['quantity']
            print(round(total_profit, 2))


def get_fewest_product():
    min_qty = float('inf')
    min_product = None
    for product_id, data in products.items():
        if data['quantity'] < min_qty:
            min_qty = data['quantity']
            min_product = data['name']
    print(min_product)


def get_most_popular_product():
    max_orders = 0
    max_product = None
    for product_id, data in products.items():
        num_orders = len(data['purchases'])
        if num_orders > max_orders:
            max_orders = num_orders
            max_product = data['name']
    print(max_product)


# main loop
while True:
    user_input = input("Enter command: ")
    tokens = user_input.split()
    command = tokens[0]
    args = tokens[1:]

    if command == 'save_product':
        save_product(*args)
    elif command == 'purchase_product':
        purchase_product(*args)
    elif command == 'order_product':
        order_product(*args)
    elif command == 'get_quantity_of_product':
        get_quantity_of_product(*args)
    elif command == 'get_average_price':
        get_average_price(*args)
    elif command == 'get_product_profit':
        get_product_profit(*args)
    elif command == 'get_fewest_product':
        get_fewest_product()
    elif command == 'get_most_popular_product':
        get_most_popular_product()
    elif command == 'exit':
        break
    else:
        print("Invalid command")