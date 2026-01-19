import heapq
from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def heaps():

def main():
    root=Node(100)
    root.left=Node(125)
    root.right=Node(250)
    root.left.left=Node(500)
    root.left.right=Node(1000)
    root.right.left=Node(2000)
    root.right.right=Node(4000)
    obj=Solution()
    res=obj.bfs(root)
    print("Result:",res)

if __name__=="__main__":
    main()
