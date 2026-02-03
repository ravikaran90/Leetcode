res=0
def recursion(nums):
        if nums<=1:
            return 1
        else:
            res==res+recursion(nums-1)
            print(res)
            return res

def main():
    res=recursion(5)
    print("Result:",res)

if __name__=="__main__":
    main()