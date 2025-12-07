class Solution:
    def valid_parentheses(self,s):
        diction={"(":")","{":"}","[":"]"}
        stack=[]
        for c in s:
            if c in "({[":
                stack.append(c)
            elif len(stack)==0:
                return False
            elif diction[stack.pop()]!=c:
                return False
        return len(stack)==0

def main():
    s="({[{()}]})"
    obj=Solution()
    res=obj.valid_parentheses(s)
    print("Result:",res)

if __name__=="__main__":
    main()