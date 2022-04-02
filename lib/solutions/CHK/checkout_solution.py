from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

min_price= float("inf")
prices={"A":50, "B":30, "C":20, "D":15, "E":40}
offers={"AAA": 130,"AAAAA":200, "BB": 45, "EEB":80}

def backtracking(idx, part_price, missing):
    global prices
    global offers
    global min_price
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
            print('jei')
    return

def checkout(skus):
    global prices
    global offers
    global min_price
    buy=Counter(skus)
    if not set(buy.keys()) <= set(prices.keys()): return -1
    #backtracking(0, 0, buy)
    return min_price






#assert checkout("AAA")==130



