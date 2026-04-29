# Tính tổng giá trị giỏ hàng
def cart_total(cart, discount=10):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]

    total = total * (1 - discount/100)
    return int(total)

cart = [
{"name": "Áo thun", "price": 120000, "quantity": 2},
{"name": "Quần dài", "price": 350000, "quantity": 1},
{"name": "Tất", "price": 25000, "quantity": 3},
] 

print(cart_total(cart, discount=10), "Vnđ")