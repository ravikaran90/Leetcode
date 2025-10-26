from collections import Counter

class Solution:
    def longest_substring_without_repetition(self,s):
        chars=Counter()
        left=0
        right=0
        res=0

        while right<len(s):
            r=s[right] #a b c d e f a b c
            chars[r]+=1
            print("Outside Loop:",chars)

            while chars[r]>1:
                l=s[left]
                chars[l]-=1
                print("Inside  Loop:",chars)
                left+=1
            print("Left:",left)
            print("Right:",right)
            res=max(res,right-left+1)
            right+=1
        string=""
        for i in chars.elements():
            string+=i
        return string

def main():
    s="abababab"
    obj=Solution()
    result=obj.longest_substring_without_repetition(s)
    print("Result:",result)

if __name__=="__main__":
    main()