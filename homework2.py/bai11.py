#Bài 11
price = 100000
percent = 20

def apply_discount(price, percent):
    apply_discount = price - (price * percent / 100)
    return apply_discount

print("Giá sau khi giảm giá là:", apply_discount(price, percent) , "vnđ")