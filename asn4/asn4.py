import os

'''
Kenny Huynh 
id: 1505024

Cmput355 Assignment 4

Solver for mazes using random walk (without remembering)

To use: 
run program by itself and it will prompt for a text file
m1.txt
m2.txt
loop.txt
straightpath.text
nosolution.txt
'''

class Maze:  
    '''
    maze solver class
    - takes a file input from the user and reads/print the maze.
    - solves the maze by using a random walk
    - maze starts at bottom left corner and end at the top right corner.
    '''
    
    def __init__(self):
        
        # row and column values
        self.row = 0           
        self.col = 0           
        self.start_row = 0      
        self.start_col = 0    
        self.end_row = 0        
        self.end_col = 0      

        done = False
        
        file = self.check_file_name()      
        maze_list = self.convert_file(file)    
            
        self._x = self.start_row       # Set the start x(row).
        self._y = 1                    # Set the start y(col).      
        
        # print the blank maze
        self.print_maze(maze_list)  

        # print the completed maze with the path
        if self.find_path(maze_list, self._x, self._y):
            done = True

        if done == False:
            print('No solution found')


    '''
    reads the file name from input
    '''    
    def check_file_name(self):
        fname = input("Enter a filename: ")  
        error = True
        # error check
        while error == True:
            # if no name was given, default file name to 'm.txt'
            if len(fname) == 0:
                fname = 'm.txt'
                print('\nOpening m.txt')  
                error = False 
            # file found
            elif os.path.isfile(fname):
                error = False       
            else:   # file not found
                fname = input("\nFile doesn't exists. Enter a new filename: ") 
                
        return fname
    
    
    '''
    converts the text file into a list to be processed
    '''    
    def convert_file(self, f):         
        maze_lst = [] 
        temp = []
        
        # Open and read the maze file
        file = open(f, 'r')
        lines = file.readlines()
        for line in lines:
            temp.append(line.strip('\n'))
        
        # find the values for row and col. 
        rc = []
        rc = temp[0].split()
        self.row = int(rc[0])*2 + 1
        self.col = int(rc[1])*2 + 1       
        temp.pop(0) 
        
        # values for the starting row and col
        self.start_row = self.row - 2
        self.start_col = 1      
        temp.pop(0)  
        
        # values for the end row and col
        end = temp[0].split() 
        self.end_row = 1
        self.end_col = self.col - 2
        temp.pop(0)  
        
        # list containing each line from the file
        for i in temp:
            maze_lst.append(list(i))
            
        file.close()  
        return maze_lst
    
    
    '''
    prints maze
    '''    
    def print_maze(self, maze_list):
        c = 0       # counter to determine if at end of the list (boundary)
        for i in maze_list:     # row
            for j in i:         # column
                
                # end of the line, print the next row
                if c == self.col:   
                    print('\n', j, end = '', sep = '')
                    c = 0               
                else:
                    print(j, end = '')                    
                c += 1
        print('\n\n')

    '''
    finding the solution of the maze
    '''
    def find_path(self, maze_list, row, col):
        
        # If we reach the end of the maze, return the maze with the solution
        if row == self.end_row and col == self.end_col:
                maze_list[row][col] = '*'
                print('Solution Found')
                self.print_maze(maze_list)
                return maze_list    

        # returns False if it encounters a wall
        if (maze_list[row][col] == '|' or
              maze_list[row][col] == '-' or
              maze_list[row][col] == '+'):
            return False     

        # returns False if it finds a prevously visited node
        if maze_list[row][col] == '*':
            maze_list[row][col] = '*'
            return False    

        # marks nodes explored with '*'
        if maze_list[row - 1][col] != '*' or\
           maze_list[row + 1][col] != '*' or\
           maze_list[row][col - 1] != '*' or\
           maze_list[row][col + 1] != '*':
            maze_list[row][col] = '*'
            
        # search the maze
        # check up, right, down, left      
        if self.find_path(maze_list, row - 1, col) or\
           self.find_path(maze_list, row, col + 1) or\
           self.find_path(maze_list, row + 1, col) or\
           self.find_path(maze_list, row, col - 1):
            return True 
        
        # any nodes that were backtracked are replaced with a blank space
        maze_list[row][col] = ' '
        return False

def main():
    maze = Maze()
    
if __name__ == "__main__":
    main()