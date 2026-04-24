#Bài 8
orders = ["A","B","A","C","A"]
dem_chu = 0

for i in orders:
    if i == "A":
        dem_chu += 1

print("A xuất hiện", dem_chu,"lần")