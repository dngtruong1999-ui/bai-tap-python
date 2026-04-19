#Bài 20
price = 1000000
is_member = True
voucher = 100000

tong_tien = 0

if is_member:
    tong_tien = (price * 0.9) - voucher
else:
    tong_tien = price - voucher

print("Tổng tiền của bạn là",tong_tien,"vnđ")