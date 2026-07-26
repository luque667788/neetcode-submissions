from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        n_islands = 0
        for s_x in range(len(grid)):
            for s_y in range(len(grid[s_x])):
                if ((s_x,s_y) not in seen) and grid[s_x][s_y] == "1":
                    # valid starting island position

                    n_islands += 1
                    # start dfs
                    to_process = deque()
                    to_process.append((s_x,s_y))

                    while len(to_process) > 0:
                        (x, y) = to_process.popleft()
                        if 0 <= x < len(grid):
                            if 0 <= y < len(grid[x]):
                                if (x,y) not in seen:
                                    if grid[x][y] == "1":
                                        seen.add((x,y))
                                        # append neighbors
                                        to_process.append((x + 1, y))
                                        to_process.append((x - 1, y))
                                        to_process.append((x, y + 1))
                                        to_process.append((x, y - 1))
        return n_islands
                        
                        

