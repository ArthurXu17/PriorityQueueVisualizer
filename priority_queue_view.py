
class PriorityQueueView(object):
    
    def __init__(self, nodes):
        self.nodes = nodes
    
    def swap(self, i, j):
        print(f"Swapping: {self.nodes[i]} and {self.nodes[j]}")
    
    def compare(self, i, j):
        print(f"Is {i} 'less than' {j}?")