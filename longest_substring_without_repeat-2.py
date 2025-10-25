from collections import Counter

class Solution:
    def longest_substring_without_repeat(self,s):
        chars=Counter()
        left=right=0
        res=0

        while right<len(s):
            r=s[right]
            chars[r]+=1

            while chars[r]>1:
                l=s[left]
                chars[l]-=1
                left+=1
            
            res=max(res,right-left+1)
            right+=1
        return res

def main():
    s="abcabrfcbb"
    obj=Solution()
    res=obj.longest_substring_without_repeat(s)
    print("Result:",res)

if __name__=="__main__":
    main()