class StackFrontier:
    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)
    
    def contains_state(self, state):
        for node in self.frontier:
            if node.state == state:
                return True
        return False

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        
    def display(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            for node in self.frontier:
                print(node.parent)