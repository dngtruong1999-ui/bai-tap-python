# Thống kê đơn hàng theo trạng thái
def count_by_status(statuses):
    result = {}

    for status in statuses:
        if status not in result:
            result[status] = 0

        result[status] += 1

    return result

statuses = [
    "confirmed", "pending", "shipped", "confirmed",
    "delivered", "pending", "cancelled",
    "confirmed", "shipped", "delivered"
]

result = count_by_status(statuses)
print(result)