#Bài 7
n = 17
so_nguyen_to = True

if n < 2:
    so_nguyen_to = False
else:
    for i in range(2, n):
        if n % i ==0:
            so_nguyen_to = False
            break

if so_nguyen_to:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")
