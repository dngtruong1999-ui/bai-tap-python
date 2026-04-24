#Bài 5
numbers = [1,2,3,4,5,6]
tong = 0
for so in numbers:
    if so % 2 == 0:
        tong += so
print("Tổng số chẵn là:", tong)
