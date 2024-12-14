class Maze:
    def __init__(self, filename):
        
        # Read file and set height and width of maze
        with open(filename) as maze_file:
            contents = maze_file.read()
        