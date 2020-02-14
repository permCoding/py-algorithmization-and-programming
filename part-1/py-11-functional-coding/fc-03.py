# генераторы списков
n = 10

lst = [0] * n
print(lst)

lst = [0 for i in range(n)]
print(lst)

lst = [i for i in range(n)]
print(lst)

lst = [i for i in range(n) if i%2==0]
print(lst)

lst = [i**2 for i in range(n)]
print(lst)
