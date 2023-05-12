'''
A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day. There are merit points associated with performing an activity each day. The same activity can’t be performed on two consecutive days. We need to find the maximum merit points the ninja can attain in N Days.

We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular day. Our task is to calculate the maximum number of merit points that the ninja can earn.

'''

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    n = len(points)
    dp = [[-1] * 4 for _ in range(n)]
    
#     def findPoints(day, merit, points, dp):
#         if(day == 0):
#             maxi = 0
#             for i in range(0,3):
#                 if merit != i:
#                     maxi = max(maxi, points[0][i])
                    
#             return maxi
#         if dp[day][merit] != -1:
#             return dp[day][merit]
#         maxi = 0
#         for i in range(0,3):
#             if merit != i:
#                 point = points[day][i] + findPoints(day-1, i, points, dp)
#                 maxi = max(maxi, point)
                
#         dp[day][merit] = maxi
#         return dp[day][merit]
#     return findPoints(n-1, 3, points, dp)
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][1], points[0][2], points[0][0])
    
    for day in range(1, n):
        for last in range(0,4):
            dp[day][last] = 0
            maxi = 0
            for i in range(0,3):
                if last != i:
                    point = points[day][i] + dp[day-1][i]
                    maxi = max(maxi, point)
            dp[day][last] = maxi
    return dp[n-1][3]