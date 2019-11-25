s1 = '18 22 21 21 19'
ages = list(map(int, s1.split()))

s2 = 'AAA BBB CCC DDD EEE FFF'
names = s2.split()

students = list(zip(names, ages))


# ages.sort()
# print(ages)
newAges = sorted(ages)
print(ages)
print(newAges)

# sorted
# sort
