from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    buy=Counter(skus)
    prices={"A":50, "B":30, "C":20, "D":15}
    offers={"A":[3, 130], "B":[2, 45]}
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
    return price


assert checkout("AAAAAv") == -1
assert checkout("A") == 50
assert checkout("B") == 30
assert checkout("AAA") == 180
assert checkout("BDBZ") == -1
assert checkout("BDB") == 60



