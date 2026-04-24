#Bài 14

def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

email = "test@gmail.com"

if is_valid_email(email):
    print("Email hợp lệ")
else:
    print("Email không hợp lệ")