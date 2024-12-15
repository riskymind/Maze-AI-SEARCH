import sys
import maze

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: Python3 maze.py maze1.txt")
    
    m = maze.Maze(sys.argv[1])
    m.print()
    # print(f"we are here {m}")

if __name__ == "__main__":
    main()
