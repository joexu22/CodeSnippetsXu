class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printData(self):
        if self.left:
            self.left.printData()
        print(self.data)
        if self.right:
            self.right.printData()

newNode = Node(22)
newNode.insert(7)
newNode.insert(25)
newNode.insert(42)

newNode.printData()