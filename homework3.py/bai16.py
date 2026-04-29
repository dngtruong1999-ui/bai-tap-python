# Gợi ý sản phẩm cùng mua (cross-sell)
def cross_sell(product_id, order_history, current_cart):
    related_products = set()
    
    for order in order_history:

        if product_id in order["items"]:
            
            for product in order["items"]:
                
                if product != product_id:
                    related_products.add(product)
    
    recommended_products = set()
    
    for product in related_products:
        if product not in current_cart:
            recommended_products.add(product)
    
    return recommended_products

order_history = [
{"items": ["SP001","SP002","SP005"]},
{"items": ["SP001","SP003"]},
{"items": ["SP001","SP002","SP004"]},
{"items": ["SP006","SP002"]},
]
current_cart = {"SP001", "SP003"}

result = cross_sell("SP001", order_history, current_cart)

print(result)