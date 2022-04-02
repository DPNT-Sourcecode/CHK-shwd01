from asyncio.windows_events import INFINITE
from collections import Counter
from re import M

# noinspection PyUnusedLocal
# skus = unicode string

min_price=INF

def backtracking(idx, offers, prices, part_price, missing):
    if missing.keys()==[]:
        if min_price>part_price: min_price=part_price
        return

    if idx==len(offers):
        for key, element in missing.items():
            if element>0: part_price+=element*prices[key]    
        if min_price>part_price: min_price=part_price
        return

    offered=offers


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




def checkout(skus):
    buy=Counter(skus)
    prices={"A":50, "B":30, "C":20, "D":15, "E":40}
    offers={"AAA": 130,"AAAAA":200, "BB": 45, "EEB":80}
    backtracking(0, offers, prices, 0, buy)
    return min_price



assert checkout("AAA")==130

