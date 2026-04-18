total_spent = 1200000

if total_spent >= 1000000:
    print("VIP")
elif total_spent < 1000000 and total_spent >= 500000:
    print("Gold")
elif total_spent <500000:
    print("Normal")