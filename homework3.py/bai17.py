# Phát hiện sản phẩm bị xóa khỏi flash sale
def sale_diff(old_sale, new_sale):
    removed = set()
    added = set()
    kept = set()
    
    for item in old_sale:
        if item not in new_sale:
            removed.add(item)
    
    for item in new_sale:
        if item not in old_sale:
            added.add(item)
    
    for item in old_sale:
        if item in new_sale:
            kept.add(item)
    
    return {
        "removed": removed,
        "added": added,
        "kept": kept
    }

old_sale = {"SP001","SP002","SP003","SP004","SP005"}
new_sale = {"SP002","SP004","SP005","SP006","SP007"}

result = sale_diff(old_sale, new_sale)
print(result)