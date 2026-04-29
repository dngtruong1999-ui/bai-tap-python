# Phân tích hành vi mua hàng theo segment
def segment_users(order_counts):
    result = {
        "one_time": set(),
        "repeat": set(),
        "vip": set()
    }
    
    for user in order_counts:
        count = order_counts[user]
        
        if count == 1:
            result["one_time"].add(user)
        elif count >= 2 and count <= 4:
            result["repeat"].add(user)
        else:
            result["vip"].add(user)
    
    return result

order_counts = {
"U001": 1, "U002": 7, "U003": 3, "U004": 1,
"U005": 5, "U006": 2, "U007": 9, "U008": 4,
}

result = segment_users(order_counts)
print(result)