string = input("comma seperated integers : ").split(',')
listvalues = map(int,string)
outputlist = list(map(lambda val: val**2, listvalues))
print(outputlist)
