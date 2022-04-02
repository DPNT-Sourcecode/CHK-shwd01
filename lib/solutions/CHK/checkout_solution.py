from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

min_price=float("inf")
prices={"A":50, "B":30, "C":20, "D":15, "E":40}
offers={"AAA": 130,"AAAAA":200, "BB": 45, "EEB":80}

def backtracking(idx, part_price, missing_aux):
    global prices
    global offers
    global min_price
    missing=missing_aux.copy()
    if missing.keys()==[]:
        if min_price>part_price: min_price=part_price
        return

    if idx==len(offers):
        for key, element in missing.items():
            if element>0: part_price+=element*prices[key]    
        if min_price>part_price: min_price=part_price
        return

    offered=list(offers.keys())[idx]
    tgt_price=offers[offered]
    backtracking(idx+1, part_price, missing.copy())
    

    if set(Counter(offered)).intersection(set(list(missing.keys()))):
        part_price+=tgt_price
        for key, element in Counter(offered).items():
            if key in missing:
                missing[key]-=element
            if missing[key]<0: del missing[key]
        backtracking(idx+1, part_price, missing.copy())
    return

def checkout(skus):
    global min_price
    min_price=float("inf")
    buy=Counter(skus)
    if not set(buy.keys()) <= set(prices.keys()): return -1
    backtracking(0, 0, buy)
    return min_price



assert checkout("AAA")==130
assert checkout("AAAAAA")==250
assert checkout("AAAAA")==200
assert checkout("AA")==100
