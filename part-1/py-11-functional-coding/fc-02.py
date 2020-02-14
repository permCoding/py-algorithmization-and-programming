lst = [1,2,3,4,5,6,7,8,9]

newMap = list(map(lambda x: x+10, lst))
print(newMap)
newFilter = list(filter(lambda x: x%2!=0, lst))
print(newFilter)

# import functools as ft
# ft.reduce
from functools import reduce

print(sum(lst))
print(reduce(lambda acc, item: acc + item, lst, 0))
print(reduce(lambda acc, item: acc + item, lst))
