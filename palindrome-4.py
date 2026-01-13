class Solution:
    def palindrome(self,string):
        left=0
        right=len(string)-1
        while left<=right:
            string[left]

def main():
    string="kayak"
    obj=Solution()
    res=obj.palindrome(string)
    print("Result:",res)

if __name__=="__main__":
    main()
