#Bài 19
cart = [200000, 1500000, 800000]

def vip_checker(cart):
    total = 0

    for item in cart:
        total = total + item

    if total >= 3000000:
        return True
    else:
        return False

print(vip_checker(cart))