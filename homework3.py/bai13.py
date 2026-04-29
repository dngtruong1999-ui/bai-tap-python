# Kiểm tra sản phẩm trong wishlist
def is_wishlisted(product_id, wishlist):
    if product_id in wishlist:
        return True
    else:
        return False

wishlist = {"SP001", "SP005", "SP012", "SP018", "SP024"}
is_wishlisted("SP005", wishlist)
is_wishlisted("SP999", wishlist)

print(is_wishlisted("SP999", wishlist))