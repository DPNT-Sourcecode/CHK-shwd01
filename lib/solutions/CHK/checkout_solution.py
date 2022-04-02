from asyncio.windows_events import INFINITE
from collections import Counter
from re import M

# noinspection PyUnusedLocal
# skus = unicode string

min_price=INF
prices={"A":50, "B":30, "C":20, "D":15, "E":40}
offers={"AAA": 130,"AAAAA":200, "BB": 45, "EEB":80}

def backtracking(idx, part_price, missing):
    if missing.keys()==[]:
        if min_price>part_price: min_price=part_price
        return

    if idx==len(offers):
        for key, element in missing.items():
            if element>0: part_price+=element*prices[key]    
        if min_price>part_price: min_price=part_price
        return

    offered=offers.keys()[idx]
    tgt_price=offers[offered]
    backtracking(idx+1, part_price, missing)
    #we only apply the offer if it makes sense
    if set(Counter(offered)).intersection(set(missing.keys())):
        part_price+=tgt_price
        for key, element in Counter(offered):
            #if key in m 



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

    backtracking(0, 0, buy)
    return min_price



assert checkout("AAA")==130


