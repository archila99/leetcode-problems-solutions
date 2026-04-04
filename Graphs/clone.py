
from collections import deque
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# 
class Solution(object):
    def bfs(self, node):
        #bfs slotution 
        if not node:
            return None

        new_nodes = {}

        # Queue for BFS
        queue = deque([node])

        #Create clone for the first node
        new_nodes[node] = Node(node.val)

        while queue:
            current = queue.popleft()

            for nei in current.neighbors:
                if nei not in new_nodes:
                    # Clone neighbor
                    new_nodes[nei] = Node(nei.val)
                    queue.append(nei)
                # Add neighbor to the cloned current node
                new_nodes[current].neighbors.append(new_nodes[nei])

            return new_nodes[node]
        
    def dfs(self, n):
        if not n:
            return None
        
        visited = {}

        def dfs(n):

            if n in visited:
                return visited[n]
            
            copy = Node(n.val)
            visited[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        

def node(adjList):
    if not adjList:
        return None
    
    # step1: create all nodes
    nodes = {}
    for i in range(len(adjList)):
        nodes[i + 1] = Node(i + 1)

    # step2: connect neighbors

    for i, neighbors in enumerate(adjList):
        for nei in neighbors:
            nodes[i + 1].neighbors.append(nodes[nei])
    
    #return node 1 as starting point
    return nodes[1]

adjList = [[2,4],[1,3],[2,4],[1,3]]

obj = Solution()
print(obj.cloneGraph(node(adjList)))
