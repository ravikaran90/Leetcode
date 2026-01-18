class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def sametree(self,root1,root2):
        if root1.val==root2.val:
            if root1.left.val==root2.left.val:
                if root1.right.val==root2.right.val:
                    return True
        else:
            return False

def main():
    root1=Node(500)
    root1.left=Node(250)
    root1.right=Node(400)
    root2=Node(500)
    root2.left=Node(250)
    root2.right=Node(400)
    obj=Solution()
    res=obj.sametree(root1,root2)
    print("Result:",res)

if __name__=="__main__":
    main()