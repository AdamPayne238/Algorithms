#!/usr/bin/python
# Start
import argparse

# Test Price Lis
# prices1 = [10, 7, 5, 8, 11, 9]


# prices2 = [100, 90, 80, 50, 20, 10]
prices = [1050, 270, 1540, 3800, 2]


# For example, find_max_profit([1050, 270, 1540, 3800, 2]) should return 3530
def find_max_profit(prices):  # Receives an input list of stock prices

    # min and max return the smallest and largest numbers in the list
    max_profit = min(prices) - max(prices)

    # Buy Price
    for buy in range(len(prices)):

        # Sell Price
        for sell in range(buy + 1, len(prices)):
            min_price = prices[buy]     # range(len(prices))
            max_price = prices[sell]    # range(buy + 1, len(prices))
            profit = max_price - min_price
            if profit > max_profit:
                max_profit = profit

    print(max_profit)
    return max_profit


# Test Cal
find_max_profit(prices)
# find_max_profit((prices2))
# find_max_profit((prices3))
if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
