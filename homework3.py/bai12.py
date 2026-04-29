# Tính phí vận chuyển theo vùng
def calc_shipping(city, weight_kg, order_total, zones):
    zone = zones.get(city, zones["other"])

    if order_total >= zone["free_threshold"]:
        return {
            "fee": 0,
            "free_shipping": True,
            "message": f"Miễn phí ship đến {city}"
        }

    fee = zone["zone_rate"] * weight_kg

    # đảm bảo phí tối thiểu
    if fee < zone["min_fee"]:
        fee = zone["min_fee"]

    fee = int(fee)

    return {
        "fee": fee,
        "free_shipping": False,
        "message": f"Phí ship đến {city}: {fee:,}đ"
    }

shipping_zones = {
    "HN": {"zone_rate": 15000, "free_threshold": 300000, "min_fee": 15000},
    "HCM": {"zone_rate": 15000, "free_threshold": 300000, "min_fee": 15000},
    "DN": {"zone_rate": 20000, "free_threshold": 350000, "min_fee": 20000},
    "other": {"zone_rate": 30000, "free_threshold": 500000, "min_fee": 30000},
}

print(calc_shipping("HN", 2, 500000, shipping_zones))