string = input("comma seperated integers : ").split(',')
listvalues = map(int,string)
outputlist = list(map(lambda val : 3*val, listvalues))
print(outputlist)
