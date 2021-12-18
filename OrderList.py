l = [(2, 1), (1, 19), (4, 5), (2, 2), (1, 3)]

for i in range(len(l)-1):
    for j in range(i,len(l)):
        if(l[i][len(l[i])-1] > l[j][len(l[j])-1]):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print('OUTPUT:- ', l)
