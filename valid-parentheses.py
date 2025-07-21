class Solution:
    def valid_par(self,string):
        diction=dict(('()','{}','[]'))
        stack=[]
        for c in string:
            if c in '({[':
                stack.append(c)
            elif len(stack)==0:
                return False
            elif c!=diction[stack.pop()]:
                return False
        if len(stack)==0:
            return True
        
def main():
    string="(({[}])]"
    obj=Solution()
    res=obj.valid_par(string)
    print("Result:",res)

if __name__=="__main__":
    main()