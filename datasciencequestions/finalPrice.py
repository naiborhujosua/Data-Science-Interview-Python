def finalPrice(prices):

    for price in range(len(prices)-1):
        for discount in range(i+1,len(prices)):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break

    return prices
