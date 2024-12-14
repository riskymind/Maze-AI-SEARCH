import stack

class QueueFrontier(stack.StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontiee")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node