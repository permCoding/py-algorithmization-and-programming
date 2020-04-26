'''
если есть два списка, то можно слить их в один zip
'''

a = ['aa', 'bbbb', 'cccccc', 'dddd', 'ee']
b = [12, 34, 56, 78, 90]

list_ab = zip(a, b)

for item in list_ab:
    print(item)
    # print("%s\t%s" % (item[1], item[0]))
    # print("{1}\t{0}".format(item[0], item[1]))