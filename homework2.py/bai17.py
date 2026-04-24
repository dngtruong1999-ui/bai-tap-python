#Bài 17
orders = [100000, 0, 200000, -50000]

def check_orders(orders):
    dem_don = 0

    for order in orders:
        if order > 0:
            dem_don = dem_don + 1

    return dem_don

print(check_orders([100000, 0, 200000, -50000]))