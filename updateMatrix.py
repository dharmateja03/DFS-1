# // Time Complexity :O(MxN)
# // Space Complexity :O(MxN)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :no


# // Your code here along with comments explaining your approach 
# Think what are you trying to achieve here , should you use bfs or dfs ? why bfs? all levels should update at same time .hwo would you track visted(this is most important) either by visted array
# or by count offset is 1.we do bfs from 0's but will only add to new level if childern are 1's
# BF would perform DFS for each one getn min in all 4 directions
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        c=0
        dir=[[0,1],[0,-1],[-1,0],[1,0]]
        m,n=len(mat),len(mat[0]) #[m][n]
        for row in range(m):
            for col in range(n):
                if mat[row][col]==0:
                    q.append((row,col))
        while(q):
            c+=1
            l=len(q)
            while(l):
                cor=q.popleft()
                
                for d in dir:
                    if -1<d[0]+cor[0]<m and -1<d[1]+cor[1]<n and mat[d[0]+cor[0]][d[1]+cor[1]]==1:
                        q.append((d[0]+cor[0],d[1]+cor[1]))
                if mat[cor[0]][cor[1]]==1:
                    
                    mat[cor[0]][cor[1]]=c
                l-=1
        for row in range(m):
            for col in range(n):
                if mat[row][col]!=0:
                    mat[row][col]-=1

        return mat
            
                            
##########################################################################################
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        res = [[0] * n for _ in range(m)]

        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        visited = [[False]*n for _ in range(m)]

        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                    res[i][j] = 0
        
        while q:
            # traverse by level
            size = len(q)
            for _ in range(size):
                x, y, dis = q.popleft()
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == 1:
                        # Expand:
                        q.append((nx, ny, dis+1))
                        mat[nx][ny] = 0
                        res[nx][ny] = dis + 1
        
        return res
                        


                        
                        


        
