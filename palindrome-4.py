class Solution:
    def palindrome(self,string):
        left=0
        right=len(string)-1
        while left<=right:
            if string[left]!=string[right]:
                return False
            left+=1
            right-=1
        return True

def main():
    string="123321"
    obj=Solution()
    res=obj.palindrome(string)
    print("Is String Palindrome:",res)

if __name__=="__main__":
    main()