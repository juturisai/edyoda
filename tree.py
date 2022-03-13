
#1. Implement Binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def display(self):
        if self.left:
            self.left.display()
        print(self.data, end=' ')
        if self.right:
            self.right.display()


def height(node):
    if node is None:
        return -1
    else:
        leftnode = height(node.left)
        rightnode = height(node.right)
        if leftnode > rightnode:
            return leftnode + 1
        else:
            return rightnode + 1


def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.data, end=' ')
        printinorder(root.right)


def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.data, end=' ')


def printpreorder(root):
    if root:
        print(root.data, end=' ')
        printpreorder(root.left)
        printpreorder(root.right)


def printleafnodes(root):
    if not root:
        return
    if not root.left and not root.right:
        print(root.data, end=" ")
        return
    if root.left:
        printleafnodes(root.left)

    if root.right:
        printleafnodes(root.right)

root = Node(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(12)
root.insert(16)
root.display()

print()
#1. Find height of a given tree

print("height is",height(root))

#3. Perform Pre-order, Post-order, In-order traversal

print("inorder: ")
printinorder(root)
print()
print("post order: ")
printpostorder(root)
print()
print("pre order: ")
printpreorder(root)
print()
#4. Function to print all the leaves in a given binary tree

print("leaf nodes: ")
printleafnodes(root)

print()
#5. Implement BFS (Breath First Search) and DFS (Depth First Search)

def BFS(root, searchvalue):
    if root is None:
        return
    que = []
    que.append(root)

    while (len(que) > 0):
        if que[0].data == searchvalue:
            print('element found', searchvalue)
            return
        node = que.pop(0)
        if node.left is not None:
            que.append(node.left)
        if node.right is not None:
            que.append(node.right)

    print('element not found')


BFS(root, 7)

found = False

def DFS(root, searchvalue):
    if root:
        if root.data == searchvalue:
            print('element found in the tree', root.data)
            global found
            found = True
        DFS(root.left, searchvalue)
        DFS(root.right, searchvalue)

def SearchDFS(root,val):
    DFS(root,val)
    if found != True:
        print('element not found')

SearchDFS(root, 10)


#6. Find sum of all left leaves in a given Binary Tree


def isleaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    else:
        return False


def sumleft(root):
    sum = 0
    if root is not None:

        if isleaf(root.left):
            sum += root.left.data
        else:
            sum += sumleft(root.left)
        sum += sumleft(root.right)
    return sum


print('sum of all left leaves', sumleft(root))

#7. Find sum of all nodes of the given perfect binary tree


def sumofnodes(root):
    sum = 0
    if root is None:
        return
    que = []
    que.append(root)

    while len(que) > 0:
        sum += que[0].data
        node = que.pop(0)
        if node.left is not None:
            que.append(node.left)
        if node.right is not None:
            que.append(node.right)
    return sum


print('sum of all nodes in the tree', sumofnodes(root))

#8. Count subtress that sum up to a given value x in a binary tree


def countsubtree(root, count, x):
    if (not root):
        return 0

    ls = countsubtree(root.left, count, x)
    rs = countsubtree(root.right, count, x)
    Sum = ls + rs + root.data
    if (Sum == x):
        count[0] += 1
    return Sum


def subtreesum(root, x):
    if (not root):
        return 0
    count = [0]
    ls = countsubtree(root.left, count, x)

    rs = countsubtree(root.right, count, x)

    if ((ls + rs + root.data) == x):
        count[0] += 1

    return count[0]


subtreesum(root, 23)

#9. Find maximum level sum in Binary Tree

def maximumlevelsum(root):
    if root == None:
        return 0

    result = root.data
    que = []
    que.append(root)

    while (len(que) > 0):
        count = len(que)
        sum = 0
        while (count > 0):
            temp = que[0]
            del que[0]
            sum += temp.data
            if temp.left != None:
                que.append(temp.left)
            if temp.right != None:
                que.append(temp.right)

            count -= 1
        result = max(sum, result)

    return result


print("Maximum level sum value is", maximumlevelsum(root))

#10. Print the nodes at oddlevel levels of a tree

def oddlevels(root, oddlevel = True):
    if root == None:
        return
    if oddlevel:
        print(root.data, end = " ")
    oddlevels(root.left, not oddlevel)
    oddlevels(root.right, not oddlevel)
print("odd level nodes")
oddlevels(root)
