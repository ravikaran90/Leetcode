class Solution:
    def reverse_vowels(self,s):
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            if s[left] not in "aeiouAEIOU":
                left+=1
            if s[right] not in "aeiouAEIOU":
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        s="".join(s)
        return s

def main():
    s="IceCreAm"
    obj=Solution()
    res=obj.reverse_vowels(s)
    print("New String:",res)

if __name__=="__main__":
    main()