# Xây dựng catalog sản phẩm
def build_catalog(products):
    catalog = {}

    for product in products:
        catalog[product["id"]] = product

    return catalog

products = [
{"id": "SP001", "name": "Áo thun basic", "price": 120000,
"category": "ao"},
{"id": "SP002", "name": "Quần jogger", "price": 280000,
"category": "quan"},
{"id": "SP003", "name": "Nón bucket", "price": 95000,
"category": "phu_kien"},
]

result = build_catalog(products)
print(result)