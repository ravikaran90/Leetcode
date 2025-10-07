class Solution:
    def number_of_islands(self,m,n,positions):
        parent={}
        land=set()

        def find(pos):
            if pos not in parent:
                return pos
            if pos!=parent[pos]:
                parent[pos]=find(parent[pos])
            return parent[pos]

        def union(pos1,pos2):
            root_pos1,root_pos2=find(pos1),find(pos2)
            if root_pos1==root_pos2: #No Action Needed
                return False
            parent[root_pos1]=root_pos2
            return True

        count=0
        res=[]

        for x,y in positions:
            if (x,y) not in land:
                land.add((x,y))
                count+=1
                for (new_x,new_y) in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                    if (new_x,new_y) in land and union((x,y),(new_x,new_y)): 
                        count-=1
            res.append(count)
        return res

def main():
    m=3
    n=3
    positions=[[0,0],[0,1],[1,2],[2,1]]
    obj=Solution()
    res=obj.number_of_islands(m,n,positions)
    print("Result:",res)

if __name__=="__main__":
    main()
