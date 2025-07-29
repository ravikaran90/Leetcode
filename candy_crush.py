class Solution:
    def candy_crush(board):
        m,n=len(board),len(board[0])
        crushed_set=set()

        def find():
            crushed_set=set()
        
        #Checking for Vertically Adjacent Candies
        for r in range(1,m-1):
            for c in range(n):
                if board[r][c]==0:
                    continue
                if board[r][c]==board[r-1][c]==board[r+1][c]:
                    crushed_set.add(r,c)
                    crushed_set(r-1,c)
                    crushed_set(r+1,c)
                    
        #Checking for Horizontally Adjacent Candies
        for r in range(m):
            for c in range(1,n-1):
                if board[r][c]==0:
                    continue
                if board[r][c]==board[r][c-1]==board[r][c+1]:
                    crushed_set.add(r,c)
                    crushed_set.add(r,c-1)
                    crushed_set.add(r,c+1)

        def crush(crushed_set):
            for r,c in range(m):
                board[r][c]=0
        


        crushed_set=find()
        while crushed_set:
            find()
            crush(crushed_set)
            crushed_set=find()
        return board

