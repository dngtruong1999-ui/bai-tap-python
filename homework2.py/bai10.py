#Bài 10

def check_login(is_logged_in):
    if is_logged_in == True:
        return "Đã đăng nhập"
    else:
        return "Chưa đăng nhập"

print(check_login(True))
