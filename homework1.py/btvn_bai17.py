base_salary = 10000000
kpi = 0.85

tong_luong = 0

if kpi >= 0.9:
    tong_luong = base_salary + base_salary*0.3
elif kpi <0.9 and kpi >= 0.8:
    tong_luong = base_salary + base_salary*0.1
else:
    tong_luong = base_salary

print("Lương tháng này của bạn là:",tong_luong,"vnđ")
