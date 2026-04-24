#Bài 12

def is_free_shipping(order_value):
    if order_value >= 50000:
        return True
    else:
        return False

print("Free ship:", is_free_shipping(60000))