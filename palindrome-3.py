class Solution: 
    def palindrome(self,string):
        left=0
        right=len(string)-1
        while left<right:
            if string[left]!=string[right]:
                return False
            left+=1
            right-=1
        return True

def main():
    string="kayak"
    obj=Solution()
    res=obj.palindrome(string)
    print("Result:",res)

if __name__=="__main__":
    main()