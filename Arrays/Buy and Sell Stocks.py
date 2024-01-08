#Buy and Sell Stocks

# def buy_and_sell_stock_once(prices):
#     min_price = 0
#     max_profit = float('inf')
#     for price in prices:
#         min_price = min(price, min_price)
#         compare_profit = price - min_price
#         max_profit = max(max_profit, compare_profit)

#     return max_profit

def buy_and_sell_stock_once(prices):
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]

    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_once(A))