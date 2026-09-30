menu = {
    'pizza' : 1800,
    'burger' : 1500,
    'hotdog' : 1000
    }

def take_order(q):
    total = 0

    print("\n===== RESTAURANT ORDER SYSTEM =====")

    name = input('Enter your name:\n')
    print('Welcome',name)

    print("\n===== MENU =====")
    
    for item, price in q.items():
        print(f"{item.title():<10} {price}")

    order = input('Enter your order:\n').lower()
    order = order.split()

    quantities = input('Enter quantities:\n')
    quantities = quantities.split()

    if len(order) != len(quantities):
        print('\nPlease enter one quantity for each item')
        return -1
    
    for i in range(len(order)):
        item = order[i]

        if item in q:
            total = total + q[item] * int(quantities[i])

        if item not in q:
            print(f"Error:'{item}'is not available in the menu")

    print("\n===== Order Summary =====")
    print('-------------------------')
    print(f'Customer: {name}')
    print(f'Order: {order}')
    print(f'Total: {total}')
    print('========================\n')
    return total

take_order(menu)



