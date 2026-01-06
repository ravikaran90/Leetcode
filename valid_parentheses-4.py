class Solution:
    def valid_parentheses(self,string):
        diction={"(":")","[":"]","{":"}"}
        stack=[]
        for i in string:
            if i in "([{":
                stack.append(i)
            elif len(stack)==0:
                return False
            elif diction[stack.pop()]!=i:
                return False
        return len(stack)==0

def main():
    string="{[()]}"
    obj=Solution()
    res=obj.valid_parentheses(string)
    print("Result:",res)

if __name__=="__main__":
    main()