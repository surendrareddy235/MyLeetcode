class node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def from_list(self,data_list):
        for val in data_list:
            self.append(val)

    def append(self,val):
        new_node = node(val)

        if not self.head:
            self.head = new_node
            return
        
        curr = self.head

        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def deleteduplicate(self):
        curr = self.head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next


ll = LinkedList()
ll.from_list([1,1,2,3,3])
ll.deleteduplicate()
print(ll.display())



            






