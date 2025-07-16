def maxprofit(day):
    # nums = []
    # profit = []
    # for i in day:
    #     nums.append(i)
    # start = nums.index(min(nums))
    # for j in nums[start:]:
    #     profit.append(j)
    # pro = max(profit)
    # if pro > start:
    #     return pro-start
    # else:
    #     return 0

# ---------------------------------------------gpt code------------------------------------->
    min_price = float('inf')
    maxprofit = 0
    for price in day:
        min_price = min(min_price,price)
        profit = price-min_price
        maxprofit = max(maxprofit,profit)
    return maxprofit
print(maxprofit([7,6,4,3,1,5]))


