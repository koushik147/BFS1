class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return [] # returning empty list
        result = [] # declaring empty list
        q = deque() 
        q.append(root) # creating and appending the root in queue
        
        while q:
            size = len(q) # getting size of q
            level = []
            for i in range(size):
                node = q.popleft() # popping the queue value and storing it in node
                level.append(node.val) # appending node value in level
                if node.left: 
                    q.append(node.left) # appending the node's left value to queue
                if node.right:
                    q.append(node.right) # appending the node's right value to queue
                    
            result.append(level) # appending the level array to result
        return result # returning result