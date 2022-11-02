#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = [] # craeting empty array
        q = deque() # creating queue
        q.append(root) # appending root value in queue
        
        while q: 
            size = len(q)
            level = [] # creating the level empty array
            for i in range(size):
                node = q.popleft() # popping the queue value and storing in node
                if node.left:
                    q.append(node.left) # appending the node's left value to queue
                if node.right:
                    q.append(node.right) # appending the node's right value to queue
                    
            result.append(node.val)# appending the level array to result
        return result # returning result
