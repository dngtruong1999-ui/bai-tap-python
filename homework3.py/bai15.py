# Lấy danh sách danh mục duy nhất
def unique_categories(products):
    result = set()
    
    for item in products:
        result.add(item["category"])
    
    return result

products = [
{"name": "Áo thun", "category": "ao"},
{"name": "Quần jean", "category": "quan"},
{"name": "Áo khoác", "category": "ao"},
{"name": "Giày", "category": "giay"},
{"name": "Áo polo", "category": "ao"},
]

print(unique_categories(products))