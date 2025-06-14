# // Time Complexity :O(MxN)
# // Space Complexity :O(MxN) + recursion stack
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :no


# // Your code here along with comments explaining your approach
# spread in all four directions from source stop if you are either at boundary or at differnt color,this check is orginalColor==color important
# Always remember what might cause for max recursion stack i.e cycle and avoid that or mark visted

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        #doing wiht bfs

        m,n=len(image),len(image[0]) #[m][n]
        q=deque()
        dir=[[0,1],[0,-1],[-1,0],[1,0]]
        q.append((sr,sc))
        orginalColor=image[sr][sc]
        if orginalColor==color:return image
        while(q):
            pos=q.popleft()
            image[pos[0]][pos[1]]=color

            #adding to q
            for d in dir:
                if -1<pos[0]+d[0]<m and -1<pos[1]+d[1]<n and image[pos[0]+d[0]][pos[1]+d[1]]==orginalColor:
                    q.append((pos[0]+d[0],pos[1]+d[1]))
        return image





#######################################################################################################################

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        def dfs(image, sr,sc,m,n,Orginalcolor,color,dir):

            #base
            if not (-1<sr<m) or not(-1<sc<n):return 
            if image[sr][sc]!=Orginalcolor:return
            #logic
            image[sr][sc]=color
            for d in dir:
                dfs(image, sr+d[0],sc+d[1],m,n,Orginalcolor,color,dir)
        if image[sr][sc]==color:return image
        m,n=len(image),len(image[0])
        dfs(image, sr,sc,m,n,image[sr][sc],color,[[0,1],[0,-1],[1,0],[-1,0]])
        return image





        
