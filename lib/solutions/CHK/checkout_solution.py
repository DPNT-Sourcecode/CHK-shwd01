from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

min_price=float("inf")
prices={"A":50, "B":30, "C":20, "D":15, "E":40, "F":10, "G":20, "H":10, "I":35,
 "J":60, "K": 80, "L":90, "M":15, "N":40, "O":10, "P":50, "Q":30, "R":50, "S":30, "T":20, "U":40, "V":50, "W":20, "X":90, "Y":10, "Z":50}
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
    trivial_offers{"A": [[5, 200], [3,]]}
    buy=Counter(skus)
    if not set(buy.keys()) <= set(prices.keys()): return -1
    backtracking(0, 0, buy)
    return min_price




Our price table and offers: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+



#assert checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWHKKEEBUUEOZXPYAVFDE")==1880