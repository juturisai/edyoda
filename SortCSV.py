fname = input("Input File Name with extension")
fields = []
data = []
with open(fname,'r') as f:
    lines = f.readlines()
    for line in lines:
        if fields == []:
            fields = (line.split(','))
        else:
            data.append(line.split(','))

fieldid =  0
rev = False

def getfield(line):
    global fieldid
    return line[fieldid]
print("please select sort by field")
for i,f in enumerate(fields):
    print(" {0}) {1}".format(i+1,f))
fieldid = int(input("enter field no: ")) - 1
if input("enter 1 to reverse sort, otherwise enter: ") == '1':
    rev = True
data.sort(key = getfield, reverse=rev)
#print(data)
with open(fname,'w') as f:
    line = ",".join(fields)
    f.write(line)
    for line in data:
        f.write(",".join(line))
