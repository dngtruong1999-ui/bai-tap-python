#Bài 4
prices=[100000,500000,700000,200000]
gia_tri_cao_nhat = prices[0]
for i in prices:
    if i > gia_tri_cao_nhat:
        gia_tri_cao_nhat = i 
print("Giá cao nhất là:",gia_tri_cao_nhat,"vnđ")
