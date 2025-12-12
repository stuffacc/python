class Node:
    data = 0
    level = 0
    child = None
    parent = None
    right = None
    
    def __init__(self, key):
        self.data = key
        self.level = 0
        self.child = None
        self.parent = None
        self.right = None
        
    def __str__(self):
        return str(self.data)
        
        
class BHeap:
    trees = []
    
    def __init__(self, trees):
        self.trees = trees
        
    def insert(self, key):
        node = Node(key)
        self.merge(BHeap([node]))
        
    def find_min(self):
        mn = 10**10
        for tree in self.trees:
            mn = min(tree.data, mn)
        
        if mn == 10**10:
            print("No min")
            return
        
        return mn
        
    def merge(self, heap):
        self.trees.extend(heap.trees)
        
        
    def extract_min(self):
        mn = 10**10
        min_node = None
        for tree in self.trees:
            if tree.data < mn:
                mn = tree.data
                min_node = tree
        
        if mn == 10**10:
            print("No min")
            return
        
        self.trees.remove(min_node)
        
        if min_node.child:
            self.merge(BHeap(min_node.child))
        
        return min_node.data
        
    def __str__(self):
        res = ""
        for tree in self.trees:
            res += str(tree) + " "
        return res
    
        
if __name__ == "__main__":
    heap = BHeap([])
    
    print(heap.find_min())
    print(heap.extract_min())
    
    
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    
    print(heap)
    print(heap.find_min())
    print(heap.extract_min())
    print(heap)
    
    print(heap.extract_min())
    print(heap)
    
    
    
