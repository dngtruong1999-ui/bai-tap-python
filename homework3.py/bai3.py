# Gợi ý sản phẩm liên quan
def related_products(product_id, products, limit=3):
    category =""

    for product in products:
        if product["id"] == product_id:
            category = product["category"]

    result = []
    for product in products:
        if product["category"] == category and product["id"] != product_id:
            result.append(product)

    result.sort(key=lambda x: x["rating"], reverse = True)

    return result[:limit]

products = [
{"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},
{"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8},
{"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2},
{"id": 4, "name": "Quần jeans","category": "quan","rating": 4.7},
{"id": 5, "name": "Áo sơ mi", "category": "ao", "rating": 4.6},
]

result = related_products(product_id=1, products=products, limit=3)
print(result)