class Solution:
    def power_of_two(self,n):
        if n==0:
            return False
        if n==1:
            return True
        elif n%2==1:
            return False
        elif n//2==1 and n%2==0:
            return True
        else:
            return self.power_of_two(n//2)

        #Scenarios
        #12 -> 6 -> 3 -> 1
        #16 -> 8 -> 4 -> 2 -> 0

def main():
    n=32
    obj=Solution()
    resu=obj.power_of_two(n)
    print("Result:",resu)

if __name__=="__main__":
    main()