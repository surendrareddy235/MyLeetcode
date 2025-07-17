from collections import deque
class tree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class symmentictree():
    def __init__(self):
        self.root = None

    def from_list(self,btlist):
        for val in btlist:
            self.append(val)

    def append(self,data):
        new_node = tree(data)

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

    def symmentric(self):
        def is_mirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return(
                t1.data == t2.data and
                is_mirror(t1.left,t2.right) and
                is_mirror(t1.right, t2.left)
            )
        return is_mirror(self.root.left,self.root.right)

    def btdisplay(self):
        def display(node):
            if not node:
                return
            display(node.left)
            print(node.data,end='-')
            display(node.right)
        display(self.root)

st = symmentictree()

st.from_list([1, 2, 2, 3, 4, 4, 3])
print(st.symmentric())
st.btdisplay()



            



            





        




