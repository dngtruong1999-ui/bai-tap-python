# Phát hiện đơn hàng bất thường
def detect_anomalies(orders, threshold):
    total = 0
    count = 0

    for order in orders:
        total += order["total"]
        count += 1

    avg = total / count

    result = []

    for order in orders:
        if order["total"] > threshold * avg:
            result.append(order)

    return result

orders = [
{"id": 101, "total": 250000},
{"id": 102, "total": 180000},
{"id": 103, "total": 920000},
{"id": 104, "total": 210000},
{"id": 105, "total": 195000},
]

result = detect_anomalies(orders, threshold=2.5)
print(result)

