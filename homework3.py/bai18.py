# Lọc review hợp lệ theo người dùng đã mua
def filter_verified_reviews(reviews, verified_buyers):
    result = []
    
    for review in reviews:
        if review["user_id"] in verified_buyers:
            result.append(review)
    
    return result

verified_buyers = {"U001", "U003", "U005", "U007"}
reviews = [
{"user_id": "U001", "rating": 5, "comment": "Rất tốt!"},
{"user_id": "U002", "rating": 1, "comment": "Kém chất lượng"},
{"user_id": "U003", "rating": 4, "comment": "Ưng ý"},
{"user_id": "U004", "rating": 5, "comment": "Tuyệt vời"},
]

result = filter_verified_reviews(reviews, verified_buyers)
print(result)