class Solution:
    def lcp(self,strs):
        if strs=="":
            return ""
        prefix=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix):
                prefix=prefix[0:len(prefix)-1]
                if prefix=="":
                    return ""
        return prefix

def main():
    strs=["ravi","ravikaran","ravikarananand"]
    obj=Solution()
    res=obj.lcp(strs)
    print("Result:",res)

if __name__=="__main__":
    main()