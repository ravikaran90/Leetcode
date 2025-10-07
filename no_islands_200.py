import collections

class Solution:
    def no_islands_200(self,grid):
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visit=set()
        islands=0

        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.pop()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands

def main():
    grid=[
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    obj=Solution()
    res=obj.no_islands_200(grid)
    print("Result:",res)

if __name__=="__main__":
    main()
