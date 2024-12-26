import sys
import maze

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: Python3 search.py maze1.txt")
    
    finder = maze.Maze(sys.argv[1])
    print("Maze: ")
    finder.print()
    print("Solving....")
    finder.solve()
        
    print("States Explored:", finder.num_explored)
    print("Solution")
    finder.print()
    finder.output_image("maze.png")
    
    
    

if __name__ == "__main__":
    main()
