#Bài 20
cart = [100000, 200000, 150000]
balance = 500000

def checkout(cart, balance):
    total = 0

    for item in cart:
        total = total + item

    if balance >= total:
        return {
            "status": "Thanh toán thành công",
            "Số dư còn lại": balance - total
        }
    else:
        return {
            "status": "Không đủ tiền",
            "Số dư còn lại": balance
        }

print(checkout(cart, balance))