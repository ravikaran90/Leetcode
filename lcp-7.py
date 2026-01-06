class Solution:
    def lcp(self,strs):
        if len(strs)=="":
            return ""
        prefix=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix):
                prefix=prefix[0:len(prefix)-1]
                if len(prefix)==0:
                    return ""
        return prefix
        

def main():
    strs=["ravikaran","ravi","ravikarananand"]
    obj=Solution()
    res=obj.lcp(strs)
    print("Longest Common Prefix:",res)

if __name__=="__main__":
    main()