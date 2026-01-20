class Solution:
    def reverse_string(self,string,k):
        newstring=""
        for i in range(len(string)-1,-1,-1):
            newstring+=string[i]
        return newstring

def main():
    string="abcdefg"
    k=2
    obj=Solution()
    res=obj.reverse_string(string,k)
    print("Result:",res)

if __name__=="__main__":
    main()


