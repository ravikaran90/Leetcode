class Solution: 
    def add_binary_strings(self,a,b):
        sum=int(a,2)+int(b,2)
        return str(bin(sum))[2:]

def main():
    a="11"
    b="1"
    obj=Solution()
    res=obj.add_binary_strings(a,b)
    print("Result:",res)

if __name__=="__main__":
    main()

