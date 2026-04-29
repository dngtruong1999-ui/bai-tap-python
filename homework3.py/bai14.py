# Tìm sản phẩm chưa được xem
def get_unviewed(all_products, viewed_products):
    result = set()
    
    for item in all_products:
        if item not in viewed_products:
            result.add(item)
    
    return result

all_products = {"SP001","SP002","SP003","SP004","SP005","SP006"}
viewed_products = {"SP001","SP003","SP005"}

print(get_unviewed(all_products, viewed_products))