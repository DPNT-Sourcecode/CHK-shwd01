from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string


+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+





def checkout(skus):
    buy=Counter(skus)
    prices={"A":50, "B":30, "C":20, "D":15, "E":40}
    offers={"A"





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


