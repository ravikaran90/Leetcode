class Solution: 
    def length_of_last_word(self,s):
        counter=0
        diction={'c':0}
        for i in range(len(s)):
            if ord(s[i])==32:
                counter=0
            else:
                counter+=1
                diction['c']=counter
        return diction['c']


def main():
    s="   fly me   to   the moon  "
    #print(chr(72))
    obj=Solution()
    res=obj.length_of_last_word(s)
    print("Result:",res)

if __name__=="__main__":
    main()