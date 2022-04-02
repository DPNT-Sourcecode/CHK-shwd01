from asyncio.windows_events import INFINITE
from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

min_price=INF

def backtracking(idx, offers, prices, part_price, missing):



def checkout(skus):
    buy=Counter(skus)
    prices={"A":50, "B":30, "C":20, "D":15, "E":40}
    offers={"AAA": 130,"AAAAA":200, "BB": 45, "EEB":80}
    backtracking(0, offers, prices, part_price, missing)
    return min_price








    if not set(buy.keys()) <= set(prices.keys()): return -1
    price=0
    for key, element in buy.items():
        price_item=0
        if key in offers:
            offer=offers[key]
            while element>=offer[0]:
                element-=offer[0]
                price_item+=offer[1]
        price_item+=element*prices[key]
        price+=price_item
    print(price)
    return price

assert checkout("AAA")==130

