"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.value)

def is_unival(root):
    return unival_helper(root, root.value)


def unival_helper(root, value):

    if root is None:
        return True

    if root.value == value:
        return unival_helper(root.left, value) and unival_helper(root.right, value)
    
    return False

# O(N^2) as we are checking subtrees again
def count_unival(root):

    if root is None:
        return 0
    
    left = count_unival(root.left)
    right = count_unival(root.right)

    return 1 + left + right if is_unival(root) else left + right



# Runtime O(N)
def count_unival_bottom_up(root):
    count, _ = helper(root)
    return count


def helper(root):

    if root is None:
        return 0, True
    
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)

    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        
        # if left is not null and its not equal to root.
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        
        # if right is not null and its not equal to root.
        if root.right is not None and root.value != root.right.value:
            return total_count, False

        # if right and left are not null and equal to root then add one        
        return total_count+1, True
    
    return total_count, False

node_a = TreeNode('0')
node_b = TreeNode('1')
node_c = TreeNode('0')
node_d = TreeNode('1')
node_e = TreeNode('0')
node_f = TreeNode('1')
node_g = TreeNode('1')
node_a.left = node_b
node_a.right = node_c
node_c.left = node_d
node_c.right = node_e
node_d.left = node_f
node_d.right = node_g

assert count_unival_bottom_up(None) == 0
assert count_unival_bottom_up(node_a) == 5
assert count_unival_bottom_up(node_c) == 4
assert count_unival_bottom_up(node_g) == 1
assert count_unival_bottom_up(node_d) == 3