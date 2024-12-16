import node
import stack

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
        
        
    def solve(self):
        """Finds a solution to maze, if only exists.""" 
        
        # Keep track of number of states explored
        self.num_explored = 0
        
        # start with a frontier that contains the initial state
        start = node.Node(state=self.start, parent=None, action=None)
        frontier = stack.StackFrontier()
        frontier.add(start)
        
        self.explored = set()
        
        while True:
            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("No Solution.")
            
            # Choose a node from the frontier
            removed_node = frontier.remove()
            self.num_explored += 1
            
            # if node is the goal, then we have a solution 
            if removed_node.state == self.goal:
                actions = []
                cells = []
                while removed_node.parent is not None:
                    actions.append(removed_node.action)
                    cells.append(removed_node.state)
                    removed_node = removed_node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            
            # Mark node as explored
            self.explored.add(removed_node.state)
            
            # Add neighbors to frontier
            for action, state in self.neighbors(removed_node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = node.Node(state=state, parent=removed_node, action=action)
                    frontier.add(child)
              
              
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
                        
                        
    def neighbors(self, current_position):
    # Extract the row and column from the current position
        row, col = current_position

    # Define possible moves and their directions
        possible_moves = [
            ("up", (row - 1, col)),    # Move up
            ("down", (row + 1, col)),  # Move down
            ("left", (row, col - 1)),  # Move left
            ("right", (row, col + 1))  # Move right
        ]

        # List to store valid moves
        valid_neighbors = []

        # Check each move to see if it is valid
        for direction, (new_row, new_col) in possible_moves:
            # Check if the new position is within the grid boundaries
            if 0 <= new_row < self.height and 0 <= new_col < self.width:
            #     # Check if the new position is not a wall
                if not self.wall[new_row][new_col]:
            #         # Add the valid move to the list
                    valid_neighbors.append((direction, (new_row, new_col)))

        # Return the list of valid moves
        return valid_neighbors

      
    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2
        
        # Create a Blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )  
        draw = ImageDraw.Draw(img)
        
        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.wall):
            for j, col in enumerate(row):
                # wall
                if col:
                    fill = (40, 40, 40)
                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)
                    
                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )
        img.save(filename)