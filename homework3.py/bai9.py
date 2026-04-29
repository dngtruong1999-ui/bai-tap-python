# Tổng hợp báo cáo doanh thu theo ngày
def daily_report(transactions):
    result = {}
    
    for item in transactions:
        date = item["date"]
        
        if date not in result:
            result[date] = {"total": 0, "count": 0}
        
        result[date]["total"] += item["amount"]
        result[date]["count"] += 1
    
    for date in result:
        total = result[date]["total"]
        count = result[date]["count"]
        result[date]["avg"] = total / count
    
    return result

transactions = [
{"date": "2024-01-15", "amount": 320000},
{"date": "2024-01-15", "amount": 185000},
{"date": "2024-01-16", "amount": 450000},
{"date": "2024-01-15", "amount": 270000},
{"date": "2024-01-16", "amount": 390000},
]

result = daily_report(transactions)
print(result)