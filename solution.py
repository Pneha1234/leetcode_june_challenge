class Solution(object):
    def invertTree(self, root):
        # check for the null value
        if not root or (not root.left and not root.right):
            return root
        # assign the value of left node to any temporary variable
        tmp = root.left
        # assign the value of left node with the right node to invert the values
        root.left = root.right
        # assign the right node with the left node value
        root.right = tmp
        
        # call the same function recursively to create a mirror image of the tree for all the child node
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
