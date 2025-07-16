class node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binarytree():
    def __init__(self):
        self.root = None

    def append(self,data):
        new_node = node(data)

        if not self.root:
            self.root = new_node
            return
        
        queue = [self.root]
        while queue:
            curr = queue.pop(0)

            if not curr.left:
                curr.left = new_node
                return 
            else:
                queue.append(curr.left)

            if not curr.right:
                curr.right = new_node
                return
            else:
                queue.append(curr.right)

    def display_inorder(self):
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.data)
                inorder(node.right)
        inorder(self.root)
        return result

bt = binarytree()
for i in range(1,10):
    bt.append(i)
print(bt.display_inorder())




