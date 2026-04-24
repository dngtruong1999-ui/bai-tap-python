#Bài 18
prices = [100000, 200000, 300000]

def total_after_discount(price):
    return price - (price * 10 / 100)

total = 0

for price in prices:
    total = total + total_after_discount(price)

print(total)