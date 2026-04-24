#Bài 16
prices = [100000, 500000, 700000, 200000]

def filter_prices(prices):
    result = []

    for price in prices:
        if price > 300000:
            result.append(price)

    return result

print(filter_prices([100000, 500000, 700000, 200000]))