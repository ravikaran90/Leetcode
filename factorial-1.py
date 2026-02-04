def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

def main():
    n=5
    res=factorial(n)
    print("Factorial of {n}:",res)

if __name__=="__main__":
    main()