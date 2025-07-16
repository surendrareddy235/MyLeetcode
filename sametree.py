from collections import deque
class node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binarytree():
    def __init__(self):
        self.root = None

    def from_list(self,btlist):
        for i in btlist:
            self.append(i)
    
    def append(self,data):
        new_node = node(data)

        if not self.root:
            self.root = new_node
            return
        
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()

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

    def displaybinary(self):
        def display(node):
            if not node:
                return
            display(node.left)
            print(node.data,end="-")
            display(node.right)
        display(self.root)

    def is_same(self,n1,n2):
        if not n1 and not n2:
            return True
        if n1 and n2 and n1.data == n2.data:
            return self.is_same(n1.left,n2.left) and self.is_same(n1.right,n2.right)
        return False 

bt1 = binarytree()
bt1.from_list([1,2,3,4,5])
bt1.displaybinary()
print()
bt2 = binarytree()
bt2.from_list([1,2,3,5])
bt2.displaybinary()
print()
print(bt1.is_same(bt1.root,bt2.root))







    
            





