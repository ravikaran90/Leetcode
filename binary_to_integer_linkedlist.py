class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution: 
    def binary_integer(self,head):
        string=""
        current=head
        while current:
            string+=str(current.val)
            current=current.next
        binary_number=int(string,2)
        return binary_number

def main():
    head=Node(1)
    head.next=Node(0)
    head.next.next=Node(1)
    obj=Solution()
    res=obj.binary_integer(head)
    print("Result:",res)

if __name__=="__main__":
    main()