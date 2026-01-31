def rc(n,diff):
    if diff>7:
        return
    else:
        print(n)
        diff+=1
        rc(n+diff,diff)

def main():
    rc(5,1)
    #5,7,10,14,19,25,32

if __name__=="__main__":
    main()