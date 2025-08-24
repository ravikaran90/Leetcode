class Solution: 
    def valid_palindrome_II(self,string):
        def checkpalindrome(string,l,r):
            while l<r:
                if string[l]!=string[r]:
                    return False
                l+=1
                r-=1
            return True
        l=0
        r=len(string)-1
        while l<r:
            if string[l]!=string[r]:
                return checkpalindrome(string,l+1,r) or checkpalindrome(string,l,r-1)
            l+=1
            r-=1
        return True

def main():
    string="abca"
    obj=Solution()
    res=obj.valid_palindrome_II(string)
    print("Result:",res)

if __name__=="__main__":
    main()