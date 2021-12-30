def sumvalues(l):
    sum = 0
    for i in l:
        sum+= i
    return sum
        
inputstring = input("enter integers : ").split(',') 
lists = list(map(int, inputstring))
print(sumvalues(lists))
