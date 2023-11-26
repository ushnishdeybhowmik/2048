import tabulate
import random
from utility import reduce_left, reduce_right, colToRows, rowsToCol
import keyboard
import time

class GameBoard:
    def __init__(self):
        self.row_1 = []
        self.row_2 = []
        self.row_3 = []
        self.row_4 = []
        self.moves = 0
   
    def set_board(self, row1:list, row2:list, row3:list, row4:list):
        self.row_1 = row1
        self.row_2 = row2
        self.row_3 = row3
        self.row_4 = row4
        
    def set_element(self, data, row_idx, col_idx):
        board = [self.row_1, self.row_2, self.row_3, self.row_4]
        board[row_idx][col_idx] = data
        self.row_1 = board[0]
        self.row_2 = board[1]
        self.row_3 = board[2]
        self.row_4 = board[3]
        
    def get_element(self, row_idx, col_idx):
        board = [self.row_1, self.row_2, self.row_3, self.row_4]
        return board[row_idx][col_idx]
        
    def get_board(self):
        return [self.row_1, self.row_2, self.row_3, self.row_4]
    
    def print_board(self):
        print(tabulate.tabulate([self.row_1, self.row_2, self.row_3, self.row_4], tablefmt="grid", numalign="center"))
        print(f"\nNo. of moves : {self.moves}\n")
        
    def move_up(self):
        columns = rowsToCol(self.row_1, self.row_2, self.row_3, self.row_4)
        col1 = reduce_left(columns[0])
        col2 = reduce_left(columns[1])
        col3 = reduce_left(columns[2])
        col4 = reduce_left(columns[3])
        self.row_1, self.row_2, self.row_3, self.row_4 = colToRows(col1, col2, col3, col4)
        self.moves = self.moves +1
        
        
    def move_down(self):
        columns = rowsToCol(self.row_1, self.row_2, self.row_3, self.row_4)
        col1 = reduce_right(columns[0])
        col2 = reduce_right(columns[1])
        col3 = reduce_right(columns[2])
        col4 = reduce_right(columns[3])
        self.row_1, self.row_2, self.row_3, self.row_4 = colToRows(col1, col2, col3, col4)
        self.moves = self.moves +1
        
    def move_left(self):
        
        self.row_1 = reduce_left(self.row_1)
        self.row_2 = reduce_left(self.row_2)
        self.row_3 = reduce_left(self.row_3)
        self.row_4 = reduce_left(self.row_4)
        self.moves = self.moves +1
        
    def move_right(self):
    
        self.row_1 = reduce_right(self.row_1)
        self.row_2 = reduce_right(self.row_2)
        self.row_3 = reduce_right(self.row_3)
        self.row_4 = reduce_right(self.row_4)
        self.moves = self.moves +1
    
    def is_board_full(self):
        full = True
        for row in [self.row_1, self.row_2, self.row_3, self.row_4]:
            for elem in row:
                if elem == 0:
                    full = False
                    return full
        return full 
    
    def game_over(self):
        self.row_1 = [0,0,0,0]
        self.row_2 = ["G", "A", "M", "E"]
        self.row_3 = ["O", "V", "E", "R"]
        self.row_4 = [0,0,0,0]

class Game():
    
    def __init__(self):
        self.gameBoard = GameBoard()
        self.gameBoard.set_board([0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0])
        while(True):
            x = random.randint(0,3)
            y = random.randint(0,3)
            #print("Hit")
            board = self.gameBoard.get_board()
            if(board[x][y] == 0):
                self.gameBoard.set_element(2, x, y)
                break
        while(True):
            x = random.randint(0,3)
            y = random.randint(0,3)
            #print("Hit")
            board = self.gameBoard.get_board()
            if(board[x][y] == 0):
                self.gameBoard.set_element(2, x, y)
                break

    def drop_tile(self):
        tile_list = [2,4]
        while(True):
            x = random.randint(0,3)
            y = random.randint(0,3)
            val = tile_list[random.randint(0,1)]
            board = self.gameBoard.get_board()
            if(self.gameBoard.is_board_full()):
                self.gameBoard.game_over()
                self.gameBoard.print_board()
                exit()
            if(board[x][y] == 0):
                self.gameBoard.set_element(str(val)+"*", x, y)
                self.gameBoard.print_board()
                self.gameBoard.set_element(val, x, y)
                return None
            

game = Game()
gameLoop = True
game.drop_tile()
while(gameLoop):
    if keyboard.is_pressed('w'):
        game.gameBoard.move_up()
        game.drop_tile()
        time.sleep(1) 
    elif keyboard.is_pressed('s'):
        game.gameBoard.move_down()
        game.drop_tile()
        time.sleep(1)
    elif keyboard.is_pressed('a'):
        game.gameBoard.move_left()
        game.drop_tile()
        time.sleep(1)
    elif keyboard.is_pressed('d'):
        game.gameBoard.move_right()
        game.drop_tile()
        time.sleep(1)
    elif keyboard.is_pressed('x'):
        gameLoop = False