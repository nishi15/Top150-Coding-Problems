'''
Definition
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of
which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbors, which
are the cells that are horizontally, vertically, or diagonally adjacent.

# Rules
# At each step in time, the following transitions occur:
# 1. Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by overcrowding.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


The initial pattern constitutes the seed of the system. The first generation is created by applying the
above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the
discrete moment at which this happens is sometimes called a tick (in other words, each generation is a
pure function of the preceding one). The rules continue to be applied repeatedly to create further
generations.


Objectives
1. Implement the game of life data structures and algorithm.
2. Demonstrate that game of life algorithm works.


Hints
 To demonstrate that the program works you can print out the state of the universe to the
console/output after each generation. There is no need to build a custom UI.
 The program must run and work properly (the working program is better than in-progress
design).
 Use the ‘Glider’ pattern placed in the middle of the 25x25 cell universe for demonstration.

'''

# Assumptions :
'''
1. Taken a 2-D inital universe state.

orig     new       Mapping in Board
0    ->   0    :     0    #dead befor -> dead after = will be dead
1    ->   1    :     1    # live befor -> live after = will be lived 
0    ->   1    :     2    # dead before -> lived after = live with "2" remark
1    ->   0    :     3    # live before -> dead after = dead "3" remark

'''

def gameOfLife(board,generation) -> None:
    
    def adjacentLiveCount(r,c): 
        live = 0
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                # skipping all out of bounds and [r,c] elements
                if ((i==r and j==c) or
                    i==rows or j==cols or i<0 or j<0  
                    ):
                    continue 
                # in both case 1 and 3 , from above assumption
                # the cell was live before , hence increment live counter
                if board[i][j] == 1 or board[i][j] == 3:  
                    live+=1 
        return live
                    

    rows, cols = len(board),len(board[0]) 
    for gen in range(1,generation+1):
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1: 
                    neighbours = adjacentLiveCount(i,j) 
                    if neighbours < 2 or neighbours > 3 : 
                        board[i][j] = 3 
                if board[i][j] == 0:
                    neighbours = adjacentLiveCount(i,j) 
                    if neighbours == 3:
                        board[i][j] = 2 
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2: 
                    board[i][j] = 1 
                if board[i][j] == 3:
                    board[i][j] = 0

        print(f"##### Printing the universe for generation {gen} #####")
        for i in range(rows):
            for j in range(cols):
                print(board[i][j],end=" ")
            print()


gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]],2)