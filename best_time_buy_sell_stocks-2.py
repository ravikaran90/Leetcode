class Solution: 
    def best_time_buy_sell_stocks(self,prices):
        min_price=float('inf')
        max_profit=0
        for i in range(len(prices)):
            if min_price>prices[i]:
                min_price=prices[i]
            elif max_profit<prices[i]-min_price:
                max_profit=prices[i]-min_price
        return max_profit

def main():
    prices=[7,6,2,4,3,11]
    obj=Solution()
    res=obj.best_time_buy_sell_stocks(prices)
    print("Result:",res)

if __name__=="__main__":
    main()