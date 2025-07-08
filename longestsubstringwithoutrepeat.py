def lengthoflongestsubstringwithoutrepeat(string):
    setofchar=set()
    count=0
    for s in string:
        if s in setofchar:
            break
        else:
            setofchar.add(s)
            count+=1
    return count

def main():
    string="abcadefghidbcbb"
    length=lengthoflongestsubstringwithoutrepeat(string)
    print("Length:",length) #Not correct output as of now

if __name__=="__main__":
    main()