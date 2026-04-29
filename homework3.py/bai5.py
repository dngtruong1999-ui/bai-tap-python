# Xếp hạng sản phẩm bán chạy theo tuần
def top_selling(item, top_n=2):
    data = {}

    for item in items:
        pid = item["product_id"]

        if pid not in data:
            data[pid] = {
                "product_id": pid,
                "name": item["name"],
                "total_qty": 0,
                "revenue": 0
            }
        data[pid]["total_qty"] += item["qty"]
        data[pid]["revenue"] += item["qty"] * item["price"]

    result = list(data.values())

    result.sort(key=lambda x: x["total_qty"], reverse = True)

    return result[:top_n]

items = [
{"product_id": 1, "name": "Áo thun", "qty": 5, "price": 120000},
{"product_id": 2, "name": "Quần jean", "qty": 3, "price": 350000},
{"product_id": 1, "name": "Áo thun", "qty": 8, "price": 120000},
{"product_id": 3, "name": "Giày", "qty": 2, "price": 450000},
{"product_id": 2, "name": "Quần jean", "qty": 4, "price": 350000},
]

result = top_selling(items, top_n=2)
print(result)