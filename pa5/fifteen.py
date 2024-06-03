# author: Sebastian Avila
# date: March  17, 2023
# file: fifteen.py is a python program that contains a class fifteen which implements a fifteen puzzle 
# input: user moves (int)
# output: game board

from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.tiles = [i for i in range(1,size**2)]
        self.tiles.append(0)
        self.adj = [[1,4],[0,2,5],[1,3,6],[2,7],[0,5,8],[1,4,6,9],[2,5,7,10],[3,6,11],[4,9,12],[5,8,10,13],
                          [6,9,11,14],[7,10,15],[8,13],[9,12,14],[10,13,15],[11,14]]

    def update(self, move):
        index_Move = self.tiles.index(move)
        index_Empty = self.tiles.index(0)
        if self.is_valid_move(move):
            self.transpose(index_Move,index_Empty)
        
    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]


    def shuffle(self, steps=100):
        index = self.tiles.index(0)
        for i in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
        
    def is_valid_move(self, move):
         index_Move = self.tiles.index(move)
         index_Empty = self.tiles.index(0)
         if index_Move in self.adj[index_Empty]:
             return True
         return False
         

    def is_solved(self):
        solved_tiles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
        if self.tiles == solved_tiles:
            return True
        return False

    def draw(self):
        print('+---+---+---+---+')
        print('|{:>2} |{:>2} |{:>2} |{:>2} |'.format(self.tiles[0] if self.tiles[0] != 0 else ' ', 
                                                    self.tiles[1] if self.tiles[1] != 0 else ' ', 
                                                    self.tiles[2] if self.tiles[2] != 0 else ' ', 
                                                    self.tiles[3] if self.tiles[3] != 0 else ' '))
                                                
        print('+---+---+---+---+')
        print('|{:>2} |{:>2} |{:>2} |{:>2} |'.format(self.tiles[4] if self.tiles[4] != 0 else ' ', 
                                                    self.tiles[5] if self.tiles[5] != 0 else ' ',
                                                    self.tiles[6] if self.tiles[6] != 0 else ' ',
                                                    self.tiles[7] if self.tiles[7] != 0 else ' '))
                                                
        print('+---+---+---+---+')
        print('|{:>2} |{:>2} |{:>2} |{:>2} |'.format(self.tiles[8] if self.tiles[8] != 0 else ' ', 
                                                    self.tiles[9] if self.tiles[9] != 0 else ' ', 
                                                    self.tiles[10] if self.tiles[10] != 0 else ' ',
                                                    self.tiles[11] if self.tiles[11] != 0 else ' '))
        print('+---+---+---+---+')
        print('|{:>2} |{:>2} |{:>2} |{:>2} |'.format(self.tiles[12] if self.tiles[12] != 0 else ' ',
                                                    self.tiles[13] if self.tiles[13] != 0 else ' ',
                                                    self.tiles[14] if self.tiles[14] != 0 else ' ',
                                                    self.tiles[15] if self.tiles[15] != 0 else ' '))
        print('+---+---+---+---+\n')
        
    def __str__(self):
        output = ''
        for i, val in enumerate(self.tiles):
            if val == 0:
                output += '   '
            elif (i+1)% 4 == 0:
                output += f'{str(val):>2}' + ' \n'
            else:
                output += f'{str(val):>2}' + ' '
        return output + '\n' if self.tiles[15] == 0 else output

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

    
    
        
