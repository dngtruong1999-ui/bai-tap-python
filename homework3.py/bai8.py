# Áp dụng mã giảm giá
def apply_coupon(cart_total, code, coupon_db):
    if code not in coupon_db:
        return {"valid": False, "message": "Mã không tồn tại"}
    
    coupon = coupon_db[code]
    
    if cart_total < coupon["min_order"]:
        return {"valid": False, "message": "Không đủ điều kiện"}
    
    if coupon["type"] == "percent":
        discount = cart_total * coupon["value"] / 100
    else:
        discount = coupon["value"]
    
    final = cart_total - discount
    
    return {
        "valid": True,
        "discount_amount": int(discount),
        "final_price": int(final),
        "message": "Áp dụng thành công"
    }

coupon_db = {
    "SALE20": {"type": "percent", "value": 20, "min_order": 200000},
    "SHIP50K": {"type": "fixed", "value": 50000, "min_order": 150000},
    "VIP30": {"type": "percent", "value": 30, "min_order": 500000},
}

result = apply_coupon(350000, "SALE20", coupon_db)
print(result)