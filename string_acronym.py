class Solution: 
    def string_acronym(self,words,s):
        string=""
        for i in range(len(words)):
            string+=words[i][0]
        if string==s:
            return True
        else:
            return False

def main():
    words=["alice","bob","charlie"]
    s="abc"
    obj=Solution()
    res=obj.string_acronym(words,s)
    print("Result:",res)

if __name__=="__main__":
    main()