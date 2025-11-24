class Solution:
    def lcp(self,string):
        if len(string)=="":
            return ""
        prefix=string[0]
        for i in range(1,len(string)):
            while string[i].find(prefix)!=0:
                string[prefix]=string[0:len(prefix)-1]
                if len(prefix)=="":
                    return ""
        return prefix

def main():
    string=["ravi","ravikaran","ravikarananand"]
    obj=Solution()
    res=obj.lcp(string)
    print("Result:",res)

if __name__=="__main__":
    main()