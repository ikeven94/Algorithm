## 주식을 사고팔기 가장 좋은 시점 (Best Time to Buy and Sell Stock)
## 한 번의 거래로 낼 수 있는 최대 이익 산출

# input
input = [7, 1, 5, 3, 6, 4]

# output
# 5

# 1일 때 사서 6일 때 팔면 5의 최대 이익

#########
# 1. BFS
#########

def maxProfit(prices) :
    max_price = 0
    for i, price in enumerate(prices):
        for j in range(i,len(prices)):
            max_price = max(prices[j] - price, max_price)
    return max_price        

print(maxProfit(input))

###########################
# 2. 저점과 현재 값과의 차이
###########################

import sys
def maxProfit2(prices):
    profit = 0
    min_price = sys.maxsize # 시스템에서 가장 큰 값 

    # 최소/ 최댓값 계속 경신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

print(maxProfit2(input))