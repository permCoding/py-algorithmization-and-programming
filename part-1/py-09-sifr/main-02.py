# 2) шифрование сдвигом

# n = 2**16-1
# print(n,chr(n))



from utils import getSifr, getDeSifr, get

s = 'Q - ПривеД, медвед!!!'
key = 666
newS = getSifr(key, s)

print(s,'\n',newS,sep='')

deSifr = getDeSifr(key,newS)

print(deSifr)


print()
newS = get(key, s)
print(newS)
deSifr = get(key,newS,-1)
print(deSifr)




# 3) шифрование ^  (>> << & ^ |)




