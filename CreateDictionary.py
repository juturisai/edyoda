i = 97
d = dict()

while True:
    d[chr(i)]=i
    if(chr(i)=='z'):
        break
    i+=1
print(d)
