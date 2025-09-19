class Solution:
    def string_reversal(self,string):
        #Reversing the String using a variable
        #ns=""
        #listing=[]
        #for i in range(len(string)-1,-1,-1):
        #    ns+=string[i]
        #for s in ns:
        #    listing.append(s)
        #return listing
        
        #Reversing the string in-place
        #string=string[::-1]
        #return string
        string=list(string)
        left=0
        right=len(string)-1
        while left<right:
            string[left],string[right]=string[right],string[left]
            left+=1
            right-=1
        return "".join(string)
        

def main():
    #string=["h","e","l","l","o"]
    string="ravi"
    obj=Solution()
    res=obj.string_reversal(string)
    print("Result:",res)

if __name__=="__main__":
    main()