# At first I solved this problem by using a recursive function (BFS), 
# but after a online research I learned about greedy algorithm, 
# and decided to implement it. Also pasted an example of dynamic programming solution, which was
# made by a leetcode user link below.

# Reference: https://leetcode.com/problems/jump-game-ii/discuss/
# problem Reference: https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: list[int]) -> int:
        # Solving the jump game II with greedy algorithm Optimal solution according to leetcode
        n = len(nums)
        if(n<2):
            return 0
        
        jump_max = nums[0]

        jump_cur = nums[0]

        jump = 1

        for i in range(1,n-1):

            jump_max = max(jump_max, i+nums[i])

            if(i==jump_cur):

                jump_cur = jump_max

                jump += 1
        
        return jump 


    def jumpBFS(self, nums: list[int]) -> int:
        # Solving the jump game II with bfs
        n = len(nums)

        if(n<2):
            return 0
        
        queue = [0]
        visited = [False]*n
        jump = 0

        while(queue):

            size = len(queue)

            for i in range(size):

                cur = queue.pop(0)

                if(cur==n-1):
                    return jump

                if(visited[cur]):
                    continue

                visited[cur] = True

                for j in range(nums[cur],0,-1):

                    if(cur+j<n):
                        queue.append(cur+j)
            
            jump += 1

    def jumpDynamic(self, nums: list[int]) -> int: # solution made by user Chenzs108 on Leetcode https://leetcode.com/problems/jump-game-ii/discuss/1455589/Python-Dynamic-Programming
        # Solving the jump game II with dynamic programming
        jmps = [math.inf for _ in range(len(nums))]
        jmps[0] = 0
        for i in range(len(nums) - 1):
            farthest = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, farthest + 1):
                jmps[j] = min(jmps[j], jmps[i] + 1)
        return jmps[-1]


        