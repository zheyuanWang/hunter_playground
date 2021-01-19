class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if grid == []: return 0
        grid_x, grid_y = len(grid),len(grid[0])
        for i in range(1,grid_x):
            grid[i][0]+=grid[i-1][0]
        for j in range(1,grid_y):
            grid[0][j]+=grid[0][j-1]
        for i in range(1,grid_x):
            for j in range(1,grid_y):
                grid[i][j]+=max(grid[i-1][j],grid[i][j-1])
        return grid[grid_x-1][grid_y-1]


"""

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5vokvr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""