class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        self.sucessor = None
        self.predecessor = None
        self.visited = set()
        
    def __del__(self):
        print(self.data, 'died')
        
    def noning(self):
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    
                    self.left = Node(data)
                    self.left.predecessor = self
                    self.left.predecessor.sucessor = self.left
                    self.left.sucessor = None
                else:     
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    self.right.predecessor = self
                    self.right.predecessor.sucessor = self.right
                    self.right.sucessor = None
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    
    def remove(self, data2):
        if self.left:
            if self.left.data == data2:
                self.noning()
            else:
                self.left.remove(data2)
        if self.right:
            if self.right.data == data2:
                self.noning()
            else:
                self.right.remove(data2)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(5)
root.insert(4)
root.insert(6)
root.insert(7)
root.insert(3)
root.remove(7)
root.PrintTree()