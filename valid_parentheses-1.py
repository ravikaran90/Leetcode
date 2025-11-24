class Solution:
    def valid_parentheses(self,string):
        diction={"(":")","{":"}","[":"]"}
        stack=[]
        for c in string:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                elif diction[stack.pop()]!=c:
                    return False
        return len(stack)==0

def main():
    string="({[]})"
    obj=Solution()
    res=obj.valid_parentheses(string)
    print("Result:",res)

if __name__=="__main__":
    main()