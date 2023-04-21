# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:return []
        stack =[]
        stack.append(root)
        ans=[]
        while stack:
            tempRoot=stack.pop()
            ans.insert(0,tempRoot.val)
            if tempRoot.left != None: stack.append(tempRoot.left)
            if tempRoot.right !=None: stack.append(tempRoot.right)
        return ans    