class Solution:
    def palindrome(self,string):
        #Not Case Sensitive
        string=string.lower()
        l=0
        r=len(string)-1
        while l<r:
            if string[l]!=string[r]:
                return False
            else:
                l+=1
                r-=1
        return True

def main():
    string="Kayakor"
    obj=Solution()
    res=obj.palindrome(string)
    print("Is String Palindrome:",res)

if __name__=="__main__":
    main()