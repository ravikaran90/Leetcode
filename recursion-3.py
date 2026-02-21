def series(num):
    if num>15:
        return
    else:
        print(num)
        series(num+1)

def main():
    res=series(5)
    print("Result:",res)

if __name__=="__main__":
    main()