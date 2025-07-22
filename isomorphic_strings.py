class Solution: 
    def isomorphic(self,s,t):
        diction1={}
        diction2={}
        for i in range(len(s)):
            if s[i] in diction1 and t[i]!=diction1[s[i]]:
                return False
            diction1[s[i]]=t[i]
            #print(diction1)
        for i in range(len(t)):
            if t[i] in diction2 and s[i]!=diction2[t[i]]:
                return False
            diction2[t[i]]=s[i]
            #print(diction2)
        return True
        

def main():
    s="egg"
    t="add"
    obj=Solution()
    res=obj.isomorphic(s,t)
    print("Are Strings isomorphic:",res)

if __name__=="__main__":
    main()
    