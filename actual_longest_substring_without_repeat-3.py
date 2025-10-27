from collections import Counter

class Solution:
    def longest_substring_without_repeat(self,s):
        chars=Counter()
        left=0
        right=0
        res=0
        substring=[]

        while right<len(s):
            r=s[right]
            chars[r]+=1
            print("Outside Loop:",chars)
            while chars[r]>1:
                l=s[left]
                print("Current String:",s[left:right+1])
                print(l)
                print("Chars of l:",chars)
                chars[l]-=1
                print("Inside Loop:",chars)
                print("--------------------------------------------------")
                left+=1
            print("Right:",right)
            print("Left:",left)
            print("Outer String:",s[left:right+1])
            res=max(res,right-left+1)
            if len(substring)<len(s[left:right+1]):
                substring=s[left:right+1]
            print("Outside Res:",res)
            right+=1
        return substring

def main():
    s="abcbcdefghifbb"
    obj=Solution()
    res=obj.longest_substring_without_repeat(s)
    print("Result:",res)

if __name__=="__main__":
    main()