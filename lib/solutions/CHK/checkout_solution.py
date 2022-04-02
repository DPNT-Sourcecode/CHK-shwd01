from collections import Counter
from itertools import combinations_with_replacement

# noinspection PyUnusedLocal
# skus = unicode string

min_price=float("inf")
prices={"A":50, "B":30, "C":20, "D":15, "E":40, "F":10, "G":20, "H":10, "I":35,
 "J":60, "K": 70, "L":90, "M":15, "N":40, "O":10, "P":50, "Q":30, "R":50, "S":20, "T":20, "U":40, "V":50, "W":20, "X":17, "Y":20, "Z":21}
offers={"AAA": 130,"AAAAA":200, "BB": 45, "EEB":80, "FFF":20, "HHHHH":45, "HHHHHHHHHH":80, "KK":120, "NNNM":120, "PPPPP":200, "QQQ":80, "RRRQ":150, "UUUU":120, "VV":90, "VVV":130}

#letters=["S", "T", "X", "Y", "Z"]

#l = list(combinations_with_replacement(letters, 3))
#for element in l:
#    offers[element[0]+element[1]+element[2]]=45


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
            if missing[key]==0: del missing[key]
            if missing[key]<0: 
                return
        backtracking(idx+1, part_price, missing.copy())
    return

def checkout(skus):
    global min_price
    global prices
    min_price=float("inf")
    buy=Counter(skus)
    if not set(buy.keys()) <= set(prices.keys()): return -1
    letters=["Z", "Y", "S", "T", "X"]
    buff=0
    buff_price=0
    price_group=0
    for element in letters:
        aux_buff=0
        if element in buy:
            aux_buff=buy[element]
            del buy[element]
            if aux_buff+buff>=3:
                buff+=aux_buff
                price_group+=45*(buff//3)
                buff = buff%3
                buff_price=buff*prices[element]
            else:
                buff_price+=prices[element]*aux_buff
                buff+=aux_buff
    
    backtracking(0, 0, buy)
    return min_price+price_group+buff_price