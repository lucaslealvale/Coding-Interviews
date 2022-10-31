# reference https://leetcode.com/problems/all-possible-full-binary-trees/solution/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    save = {0: [], 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        if n not in Solution.save:
            resp = []
            for i in range(0,(n),1):
                cond = n - 1 -i
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(cond):
                        aux = TreeNode(0)
                        aux.left = left
                        aux.right = right
                        resp.append(aux)
            Solution.save[n] = resp
        return Solution.save[n]