class Maze:
    
    def __init__(self, filename):
        self.solution = None
        
        # Read file and set height and width of maze
        with open(filename) as maze_file:
            contents = maze_file.read()
            
            # Validate start and goal
            if contents.count("A") != 1:
                raise Exception("maze must have exactly one start point")
            if contents.count("B") != 1:
                raise Exception("maze must have exactly one goal")
            
            # Determine height and width of maze
            contents = contents.splitlines()
            self.height = len(contents)
            self.width = 0
            for line in contents:
                if len(line) > self.width:
                    self.width = len(line)
            
            # Keep track of walls
            self.wall = []
            for i in range(self.height):
                row = []
                for j in range(self.width):
                    try:
                        if contents[i][j] == "A":
                            self.start = (i, j)
                            row.append(False)
                        elif contents[i][j] == "B":
                            self.goal = (i, j)
                            row.append(False)
                        elif contents[i][j] == " ":
                            row.append(False)
                        else:
                            row.append(True)
                    except IndexError:
                        row.append(False)
                self.wall.append(row)
            
            
    
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.wall):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")  
            print()
        print()
                        
        