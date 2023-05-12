#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        # dp = [[-1] * N for _ in range(N)]
        # def findMinPartition(i, j, arr, dp):
        #     mini = 10 ** 9
        #     if i==j:
        #         return 0
        #     if dp[i][j] != -1:
        #         return arr[i][j]
                
        #     for k in range(i, j):
        #         steps = arr[i-1] * arr[k] * arr[j] + findMinPartition(i, k, arr, dp)+ findMinPartition(k+1, j, arr, dp)
        #         if steps < mini:
        #             mini = steps
                
        #     dp[i][j] = mini
        #     return dp[i][j]
                
        # return findMinPartition(1, N-1, arr, dp)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0
            
        for i in range(N-1, 0, -1):
            for j in range(i+1, N):
                mini = 10 ** 9
                for k in range(i, j):
                    steps = arr[i-1] * arr[k] * arr[j] + dp[i][k] + dp[k+1][j]
                    if steps < mini:
                        mini = steps
                        
                dp[i][j] = mini
                
        return dp[1][N-1]