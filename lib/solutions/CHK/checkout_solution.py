from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

min_price=float("inf")
prices={"A":50, "B":30, "C":20, "D":15, "E":40, "F":10, "G":20, "H":10, "I":35,
 "J":60, "K": 80, "L":90, "M":15, "N":40, "O":10, "P":50, "Q":30, "R":50, "S":30, "T":20, "U":40, "V":60, "W":20, "X":90, "Y":10, "Z":50}
offers={"AAA": 130,"AAAAA":200, "BB": 45, "EEB":80, "FFF":20, "HHHHH":45, "HHHHHHHHHHH":80, "KK":150, "NNNM":120, "PPPPP":200, "QQQ":80, "RRRQ":150, "UUUU":120, "VV":90, "VVV":130}


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
    

    while set(Counter(offered)).intersection(set(list(missing.keys()))):
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


assert checkout("AAAAAA")==250
assert checkout("AAAAA")==200
assert checkout("AA")==100
assert checkout("BB")==45
assert checkout("B")==30
assert checkout("bBB")==-1
assert checkout("BBBBB")==120
assert checkout("EEB")==80
assert checkout("EE")==80
assert checkout("BEBE")==110
assert checkout("HHHHHHHHHHH")==80
assert checkout("HHKHHHKHHHHHH")==230
assert checkout("RRRQQQ")==210
#assert checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWHKKEEBUUEOZXPYAVFDE")==1880