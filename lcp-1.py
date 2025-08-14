class Solution: 
    def lcp(self,strs):
        if len(strs)==0:
            return ""
        prefix=strs[0]
        for i in range(len(strs)):
            while strs[i].find(prefix)!=0:
                prefix=prefix[0:len(prefix)-1]
                if len(prefix)==0:
                    return ""
        return prefix

def main():
    strs=["ravikaran1","ravikaran1","ravikaran1anand"]
    obj=Solution()
    res=obj.lcp(strs)
    print("Result:",res)

if __name__=="__main__":
    main()