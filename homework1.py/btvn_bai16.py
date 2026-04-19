kwh = 300
tong_tien = 0

bac_1 = 1678 #(0-50)
bac_2 = 1734 #(51-100)
bac_3 = 2014 #(101-200)

if kwh <= 50:
    tong_tien = kwh*bac_1
elif kwh > 50 and kwh <= 100:
    tong_tien = 50*bac_1 + (kwh - 50)*bac_2
elif kwh > 100:
    tong_tien = 50*bac_1 + 50*bac_2 + (kwh-100)*bac_3
print("Tổng tiền của bạn là:",tong_tien,"vnđ")

