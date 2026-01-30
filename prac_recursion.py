def nums_rec(n):
    if n<1:
        return 1
    else:
        print(n)
        return nums_rec(n-1)

def nums_itr(n):
    while n>0:
        print(n)
        n-=1

def main():
    res=nums_rec(5)
    #print(res)
    nums_itr(5)

if __name__=="__main__":
    main()