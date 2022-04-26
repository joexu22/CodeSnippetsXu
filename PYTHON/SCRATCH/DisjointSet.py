# Union Find Class Disjoint Set
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def find(self, x):
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
# Test Cases
if __name__ == "__main__":
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)
    uf.union(3, 5)
    uf.union(4, 5)
    print(uf.connected(1, 6))
    print(uf.connected(1, 5))
    print(uf.connected(1, 4))