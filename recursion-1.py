def rec(n):
    if n>10:
        return 11
    else:
        print(n)
        rec(n+1)

def main():
    n=1
    rec(n)

if __name__=="__main__":
    main()