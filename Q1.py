n = int(input())
prices = list(map(int, input().split()))

def calculate_max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        potential_profit = price - min_price
        max_profit = max(max_profit, potential_profit)    
    return max_profit

print(calculate_max_profit(prices))
