# Datastructure to hold information 
# Nodes are simply a data structure — they don’t search, they hold information.
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        