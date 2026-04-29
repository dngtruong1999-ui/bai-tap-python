# Lọc sản phẩm còn hàng
def filter_available(products):
    result = []
    for product in products:
        if product["stock"] > 0 and product["is_active"] == True:
            result.append(product)
    return result

products = [
{"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
{"id": 2, "name": "Quần jean", "stock": 0, "is_active": True},
{"id": 3, "name": "Giày sneaker","stock": 5, "is_active": False},
{"id": 4, "name": "Nón baseball","stock": 3, "is_active": True},
] 

print(filter_available(products))  