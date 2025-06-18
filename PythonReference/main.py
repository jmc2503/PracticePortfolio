from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.current = self
    
    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            res = self.current
            self.current = self.current.next
            return res
        
    

class DoubleListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:
            self.min -= pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return self.min + top
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
    
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, pos):
        while pos > 0:
            parent_pos = self.get_parent_pos(pos)
            if self.heap[pos] < self.heap[parent_pos]:
                self.heap[pos], self.heap[parent_pos] = self.heap[parent_pos], self.heap[pos]
                pos = parent_pos
            else:
                break


    def peek(self):
        return self.heap[0]

    def get_parent_pos(self, i):
        return (i - 1) // 2

def list_methods():
    A = [1, 2, 3, 4, 5, 6, 7]
    B = [3, 3, 5, 100, 2]

    A.append(9) #append new element
    #A.clear() #empty the list
    A.copy() #copy the list
    A.count(3)
    A.extend(B) #smash two iterables together
    print(A)
    A.index(3) #returns the index of the first element with this value
    A.insert(2, 3) # puts the element 3 at position 2
    A.pop() #removes element at specified position
    A.remove(1) #removes the first element with that value
    A.reverse() #reverses the list
    A.sort() #sorts the list

def string_methods():
    A = "hello"

    A.capitalize() #converts first letter to uppercase
    A.casefold() #converts letter to lowercase
    A.center(20, "O") #makes string A of length 20 with padded O's to put A in the center
    A.count("he") #returns the number of times the substring appears
    A.index("l") #returns position of where "l" is found
    ["h", "e", "l", "l", "o"].join() #turns list into string
    "what is going on".split()
    A.startswith("h")
    A.endswith("o")

def dict_methods():
    A = {}
    A.get("fortnite", 0) #look for key, if not there, give it default value
    A.items()
    A.keys() #returns all keys
    A.pop("fortnite") #removes key and returns value
    A.values() #returns all values

    B = defaultdict(list)


def dfs(root):
    if root == None:
        return
    
    left = dfs(root.left)
    right = dfs(root.right)

def bfs(root):
    if root is None:
        return
    
    q = []
    res = []

    q.append(root)
    curr_level = 0

    while q:
        len_q = len(q)
        res.append([])

        for _ in range(len_q):
            node = q.pop(0)
            res[curr_level].append(node.val)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)

        curr_level += 1
    
    return res

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start):
        visited = [False] * (len(self.graph) + 1)
        
        queue = []

        queue.append(start)
        visited[start] = True

        while queue:
            s = queue.pop(0)
            print(s, end= " ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

x = ListNode(0, None)
y = ListNode(1, None)
z = ListNode(2, None)
x.next = y
y.next = z

for node in x:
    print(node)


def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        raise ValueError("Divide by 0")
    return x / y

