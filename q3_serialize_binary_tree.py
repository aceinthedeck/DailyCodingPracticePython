"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.value)

#BFS
def serialize(root):
    
    node_list = []
    if not root:
        return ''
    
    queue = []
    
    queue.append(root)

    while queue:

        for i in range(len(queue)):
            currentNode = queue.pop(0)

            if currentNode:
                node_list.append(currentNode.value)
                queue.append(currentNode.left)
                queue.append(currentNode.right)
            
            else:
                node_list.append(None)
    
    serial_tree = ",".join([str(x) for x in node_list])
    return serial_tree

#BFS
def deserialize(tree):
    tree = tree.split(",")

    if tree[0] == "None":
        return None

    queue = []

    root = TreeNode(int(tree[0]))

    queue.append(root)

    i = 1
    while queue:

        for _ in range(len(queue)):
            currentNode = queue.pop(0)
            
            if tree[i] == "None":
                currentNode.left = None
            else:
                currentNode.left = TreeNode(int(tree[i]))
                queue.append(currentNode.left)
            
            i = i + 1

            if tree[i] == "None":
                currentNode.right = None
            else:
                currentNode.right = TreeNode(int(tree[i]))
                queue.append(currentNode.right)
            
            i = i + 1

    return root


#DFS
def serialize_dfs(root):
    if root is None:
        return None
    
    serial_tree_list = []

    dfs(root, serial_tree_list)
    serial_tree = ",".join([str(x) for x in serial_tree_list])
    return serial_tree
    


def dfs(node, serial_tree_list):

    if node is None:
        serial_tree_list.append(None)
        return
    
    serial_tree_list.append(node.value)
    dfs(node.left, serial_tree_list)
    dfs(node.right, serial_tree_list)

def deserialize_dfs(tree):
    tree = tree.split(",")
    current_index = [0]
    return dfs_recursive(tree, current_index)

def dfs_recursive(node_list, current_index):
    if node_list[current_index[0]] == "None":
        current_index[0] = current_index[0] + 1
        return None
    
    x = TreeNode(int(node_list[current_index[0]]))
    current_index[0] = current_index[0] + 1
    x.left = dfs_recursive(node_list, current_index)
    x.right = dfs_recursive(node_list, current_index)
    return x
        


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)

#text_tree = serialize(root)

#root = deserialize(text_tree)

#print(serialize(root))

text_tree = serialize_dfs(root)

root = deserialize_dfs(text_tree)

print(serialize(root))



        

