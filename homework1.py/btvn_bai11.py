#Bài 11
order_value = 180000
shipping_fee = 30000
total = order_value

if total >= 200000:
    print("Bạn được free ship, và tổng tiền của bạn là: ",total,"vnđ")
elif total < 200000:
    print("Phí ship của bạn là: ",shipping_fee,"vnđ")
    print("Tổng tiền của bạn là: ",total + shipping_fee,"vnđ")