#Bài 3
prices = [100000,500000,700000,200000]
dem_so = 0 
for i in prices:
    if i > 300000:
        dem_so = dem_so + 1
print("Các giá trị lớn hơn 300000 là:", dem_so)
