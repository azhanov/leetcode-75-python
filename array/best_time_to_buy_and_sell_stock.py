

class SolutionNaive(object):
    """
    Iterate over every number and again in the inner loop, searching forward from the current price, while keeping
     track which combo gives the max profit.

    O(N^2) time complexity - double loop
    O(1) space complexity - not using any additional DS
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for idx, buy_price in enumerate(prices):
            for idx_inner in range(idx, len(prices)):
                sell_price = prices[idx_inner]
                cur_profit = sell_price - buy_price
                if cur_profit > max_profit:
                    max_profit = cur_profit
        return max_profit


class SolutionBest(object):
    """
    Summary: find the low and keep calculating max possible profit going forward, if find lower low -
    reset min_price and search for better profit

    Visual representation of 7, 1, 5, 3, 6, 4
     \
      \                 /\
       \        /\     /  \
        \      /  \  /     \
         \    /    \/
          \  /
           \/

    O(N) time complexity - single pass
    O(1) space complexity - not using any additional DS
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return None
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                if price - min_price > max_profit:
                    max_profit = price - min_price
        return max_profit


if __name__ == '__main__':
    s = SolutionNaive()
    s = SolutionBest()
    assert (s.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
