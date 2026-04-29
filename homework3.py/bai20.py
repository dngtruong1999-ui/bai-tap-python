# Kiểm tra xung đột kho hàng trong flash sale
def check_conflicts(flash_sale_items, active_campaigns):
    conflicts = {}
    safe_items = set()

    for item in flash_sale_items:
        found = []
        is_conflict = False

        for campaign_name in active_campaigns:
            campaign_products = active_campaigns[campaign_name]

            if item in campaign_products:
                found.append(campaign_name)
                is_conflict = True

        if is_conflict == True:
            conflicts[item] = found
        else:
            safe_items.add(item)

    has_conflict = False
    if len(conflicts) > 0:
        has_conflict = True

    return {
        "has_conflict": has_conflict,
        "conflicts": conflicts,
        "safe_items": safe_items
    }

active_campaigns = {
"clearance": {"SP001","SP005","SP009"},
"bundle_deal": {"SP003","SP007","SP011"},
"new_arrival": {"SP013","SP015"},
}
flash_sale_items = {"SP001","SP003","SP007","SP020","SP025"}

result = check_conflicts(flash_sale_items, active_campaigns)
print(result)