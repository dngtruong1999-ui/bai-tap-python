#Bài 15
orders = [100000, 200000, 300000]

def total_revenue(orders):
    total = 0

    for order in orders:
        total = total + order
    
    return total

print(total_revenue(orders))