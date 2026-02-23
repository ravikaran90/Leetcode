def recursion(num):
    if num<5:
        return
    else:
        print(num)
        recursion(num-1)

def main():
    recursion(20)

if __name__=="__main__":
    main()
