#Bài 13

def classify_customer(total_spent):
    if total_spent >= 1000000:
        return "VIP"
    elif total_spent >= 500000:
        return "Gold"
    elif total_spent < 500000:
        return "Normal"

print(classify_customer(1200000))