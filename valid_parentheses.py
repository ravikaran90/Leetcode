class Solution: 
    def valid_parentheses(self,string):
        stack=[]
        diction={"(":")","{":"}","[":"]"}
        for s in string:
            if s in "([{":
                stack.append(s)
            elif len(stack)==0:
                return False
            elif s!=diction[stack.pop()]:
                return False
        if len(stack)==0:
            return True

def main():
    string="()[]{}"
    obj=Solution()
    res=obj.valid_parentheses(string)
    print("Result:",res)

if __name__=="__main__":
    main()