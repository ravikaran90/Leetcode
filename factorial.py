def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def main():
    res=factorial(5)
    #5*4*3*2*1
    print(res)

if __name__=="__main__":
    main()