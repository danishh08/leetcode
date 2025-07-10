class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        island_sizes = defaultdict(int)  
        island_id = 2  
        max_size = 0  

        def dfs(i, j, id):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0 
            grid[i][j] = id  
            size = 1 
            for dx, dy in dirs:
                size += dfs(i + dx, j + dy, id) 
            return size

      
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)  
                    island_sizes[island_id] = size 
                    max_size = max(max_size, size) 
                    island_id += 1  

      
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()  
                    current_size = 1  

                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            neighbor_id = grid[ni][nj]  
                            if neighbor_id not in neighbors:  
                                current_size += island_sizes[neighbor_id]   
                                neighbors.add(neighbor_id)  
                    
                    max_size = max(max_size, current_size)

      
        return max_size if max_size != 0 else n * n