class Solution:
    def fib(self,n):
        if n<=1:
            return 1
        else:
            return self.fib(n-2)+self.fib(n-1)

def main():
    obj=Solution()
    res=obj.fib(5)
    print("Result:",res)

if __name__=="__main__":
    main()