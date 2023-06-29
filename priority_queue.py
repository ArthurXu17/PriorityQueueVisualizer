def get_left_child(index):
    return 2 * index + 1

def get_right_child(index):
    return 2 * index + 2

def get_parent(index):
    return (index - 1) // 2
    

class PriorityQueue(object):
    
    def __init__(self, less_than):
        self.less_than = less_than
        self.nodes = []
    
    def _min(self, a, b):
        if self.less_than(a, b):
            return a
        else:
            return b
    
    def _max(self, a, b):
        if self.less_than(a, b):
            return b
        else:
            return a
    
    def size(self):
        return len(self.nodes)
    
    def _in_range(self, index):
        return 0 <= index < self.size()
    
    def _fix_up(self, index):
        """
            appended new element at [index] in the array, move upwards until parent is smaller
        """
        while self._in_range(get_parent(index)) and self.less_than(self.nodes[index], self.nodes[get_parent(index)]):
            temp = self.nodes[index]
            self.nodes[index] = self.nodes[get_parent(index)]
            self.nodes[get_parent(index)] = temp
            index = get_parent(index)
    
    def _fix_down(self, index):
        while self._in_range(get_left_child(index)):
            # finding smaller child
            smallerChild = get_left_child(index)
            if (not smallerChild == self.size() - 1) and self.less_than(self.nodes[smallerChild + 1], self.nodes[smallerChild]):
                smallerChild = smallerChild + 1
            
            # swap smaller child with cur index if necessary
            if self.less_than(self.nodes[index], self.nodes[smallerChild]):
                break
            
            self.nodes[index], self.nodes[smallerChild] = self.nodes[smallerChild], self.nodes[index]
            index = smallerChild 
        
    
    def get_min(self):
        return self.nodes[0]
    
    def insert(self, val):
        self.nodes.append(val)
        self._fix_up(self.size() - 1)
    
    def delete_min(self):
        ret_val = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()
        self._fix_down(0)
        return ret_val