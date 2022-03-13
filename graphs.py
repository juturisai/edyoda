class Graph:

    def __init__(self):
        self.graph = dict()
        self.V = set()

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = list()
            self.graph[u].append(v)
        self.V.add(u)
        self.V.add(v)

    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1)
        queue = [s]
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            if s in self.graph:
                for i in self.graph[s]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True

    def DFS(self, v, visited=set()):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)

    def isCyclic(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclic(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True

        recStack[v] = False
        return False

    def cyclic(self):

        visited = [False] * (len(self.V) + 1)
        recStack = [False] * (len(self.V) + 1)
        for node in range(len(self.V)):
            if not visited[node]:
                if self.isCyclic(node, visited, recStack):
                    return True
        return False


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(0, 3)
graph.addEdge(0, 2)
graph.addEdge(1, 3)

# 1.Breadth First Traversal for a Graph

print("find element by BFS")
graph.BFS(3)
print()
# 2. Depth First Traversal for a Graph

print("find element by DFS")
graph.DFS(3)

# 5. Detect Cycle in a Directed Graph
graph.cyclic()


# 3. Count the number of nodes at given level in a tree using BFS

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
        print(self.data)
        if self.right:
            self.right.display()


root = Node(10)
root.insert(15)
root.insert(8)
root.insert(5)
root.insert(6)
root.insert(12)
root.insert(19)


def findallnodesatgivenlevel(root, level):
    if root is None:
        return 0

    result = root.data
    q = [root]

    while len(q) > 0:
        count = len(q)
        if level == 0:
            print(count)
        level -= 1
        while count > 0:
            temp = q[0]
            del q[0]
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)

            count -= 1


findallnodesatgivenlevel(root, 2)


# 4. Count number of trees in a forest

def addedge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def DFS(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if not visited[adj[u][i]]:
            DFS(adj[u][i], adj, visited)


def counttrees(adj, V):
    visited = [False] * V
    out = 0
    for u in range(V):
        if not visited[u]:
            DFS(u, adj, visited)
            out += 1
    return out


V = 6
adj = [[] for i in range(V)]
addedge(adj, 0, 1)
addedge(adj, 0, 2)
addedge(adj, 2, 3)
addedge(adj, 3, 4)
print(counttrees(adj, V))

# Implement n-Queen’s Problem

def checksafe(board, r, c):
    for i in range(c):
        if board[r][i] == 1:
            return False

    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(r, N, 1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQ(board, c):
    if c >= N:
        return True
    for i in range(N):
        if checksafe(board, i, c):
            board[i][c] = 1
            if solveNQ(board, c + 1):
                return True
            board[i][c] = 0
    return False


def solve(board):
    if not solveNQ(board, 0):
        print("Solution does not exist")
        return False
    return True


N = 4
board = []
for i in range(N):
    t = [0 for j in range(N)]
    board.append(t)

if solve(board):

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
