class Solution: 
    def add_binary(self,a,b):
        sum=int(a,2)+int(b,2) #String to Integer
        res=str(bin(sum)) #Integer to Binary to String
        return res[2:] # Return from 3rd character onwards

def main():
    a="11"
    b="1"
    obj=Solution()
    res=obj.add_binary(a,b)
    print("Result:",res)

if __name__=="__main__":
    main()