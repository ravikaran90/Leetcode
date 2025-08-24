class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution: 
    def palindrome_linkedlist(self,head):
        listing=[]
        while head:
            listing.append(head.val)
            head=head.next
        l=0
        r=len(listing)-1
        while l<r:
            if listing[l]!=listing[r]:
                return False
            l+=1
            r-=1
        return True

def main():
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(2)
    head.next.next.next=Node(1)
    obj=Solution()
    res=obj.palindrome_linkedlist(head)
    print("Result:",res)

if __name__=="__main__":
    main()