#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque() # creating queue
        q.append(root) # appending root in queue
        
        while q:
            size = len(q)
            level = [] # creating empty array
            for i in range(size): 
                curr = q.popleft() # storing the value in curr by popping in queue
                if curr!=None:
                    level.append(curr.val) # appending the curr value in level
                    q.append(curr.left) # appending the node's left value to queue
                    q.append(curr.right) # appending the node's right value to queue
                else:
                    level.append(curr) # appending curr value to level
            if not (self.isPalin(level)): # if ispalin of level is not true then return false
                return False
        return True
    
    def isPalin(self,li):
        left=0 # assigning left to 0
        right = len(li)-1 # assigning right to lenfth of li
        while left<=right: # if left is less than right
            if li[left]!=li[right]: # if li[left] is not equal to li[right]
                return False
            left+=1 # increment by 1
            right-=1 # decrement by 1
        return True
