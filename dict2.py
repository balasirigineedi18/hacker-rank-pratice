# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    entry = input().rsplit(' ', 1)
    item_name = entry[0]
    price = int(entry[1])

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item, net_price in items.items():
    print(item, net_price)
