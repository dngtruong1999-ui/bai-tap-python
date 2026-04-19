#Bài 18
distance = 12

#1km đầu tiên 15000
#2-10km 12000/km
#>10km  10000/km

tien_xe = 0

if distance <=1:
    tien_xe = 15000
elif distance >=2 and distance <=10:
    tien_xe = 15000 + (distance-1)*12000
else:
    tien_xe = 15000 + (distance-1)*12000 + (distance-11)*10000

print("Tiền xe của bạn là:",tien_xe,"vnđ")