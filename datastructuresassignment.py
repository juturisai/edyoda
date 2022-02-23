#question no 1

l = list(map(int,input("space seperated numbers").split()))
sumvalue = int(input('sum value'))
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i] + l[j] == sumvalue:
            print('({0},{1})'.format(l[i],l[j]))

#question 2
ary = [3,4,5,6]
n = len(ary)
for i in range(n//2):
    temp = ary[i]
    ary[i] = ary[n-1-i]
    ary[n-1-i] = temp
print(ary)


#question 3
s1 = "ABCD"
s2 = 'DCBA'
print(s1[::-1] == s2)

#question 4
from collections import Counter
s = 'djfdfgsjlshfg'
dic = Counter(a)
for i in s:
    if dic[i] == 1:
        print(i)
        break


#question 5
def hanoi(n , s, d, a):
    if n==1:
        print ("Move disk 1 from source",s,"to destination",d)
        return
    hanoi(n-1, s, a, d)
    print ("Move disk",n,"from source",s,"to destination",d)
    hanoi(n-1, a, d, s)

n = 4
hanoi(n,'a','b','c')

#question 6
def fn(postfix):
    s = []  
    for i in range(len(postfix)): 
        if postfix[i] not in '+-*/':
            s.append(postfix[i])  
        else:  
            v1 = s.pop()  
            v2 = s.pop()  
            exp = postfix[i] + v2 + v1  
            s.append(exp)  
    return s.pop()  
print(fn('ABC*+'))

#question 7
def fn(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if prefix[i] not in "*+-/^()":
            stack.append(prefix[i])
            i -= 1
        else:
            stack.append("{} {} {}".format(stack.pop(), prefix[i], stack.pop()))
            i -= 1
    return stack.pop()


print(fn("*BC"))


#question 8
from collections import Counter
s = '((a+b)*c)/d'
l = []
for i in s:
    if i in '(){}[]':
        if i in '({[':
            l.append(i)
        else:
            try:
                popv = l.pop()
                if popv == '(' and i == ')':
                    pass
                elif popv == '[' and i == ']':
                    pass
                elif popv == '{' and i == '}':
                    pass
                else:
                    print('invalid expression')
            except:
                print('invalid expression')
if l != []:
    print('invalid expression')
else:
    print('valid expression')

#question 9
stack = [2,5,36,9,7,1,5,6]

def Reverse(s): 
    if s == []:
        pass
    else:
        popped = s.pop()
        Reverse(s)
        s.insert(0,popped)
Reverse(stack)
print(stack)

#question 10

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
        
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
    

    def MinValue(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element = {0}" .format(self.minimum))


    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value

        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node


    def pop(self):
        if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print(self.minimum)
                self.minimum = ( ( 2 * self.minimum ) - removedNode )
            else:
                print (removedNode)


s = Stack()

s.push(10)
s.push(25)
s.push(11)
s.push(12)
s.MinValue()

