# author: Sebastian Avila
# date: February 7, 2023
# file: board.py is a python program that contains a board class for a tictactoe game. 
# input: user response and sign (strings)
# output: input prompts and game moves

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""

      def get_size(self): 
                  # optional, return the board size (an instance size)
                  return self.size
                  
      def get_winner(self):
            # return the winner's sign O or X (an instance winner)     
            return self.winner

      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            valid_choices = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
            index = valid_choices.index(cell.upper())
            self.board[index] = sign
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            valid_choices = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
            index = valid_choices.index(cell.upper())
            return True if self.board[index] == ' ' else False
            
      def isdone(self):
            done = False
            self.winner = ''
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            if (self.board[0] == self.board[1] == self.board[2] and self.board[0] != ' '):
                  self.winner  = self.board[0]
                  done = True
            elif (self.board[3] == self.board[4] == self.board[5] and self.board[3] != ' '):
                  self.winner  = self.board[3]
                  done = True
            elif (self.board[6] == self.board[7] == self.board[8] and self.board[6] != ' '):
                  self.winner  = self.board[6]
                  done = True
            elif (self.board[0] == self.board[3] == self.board[6] and self.board[0] != ' '):
                  self.winner  = self.board[0]
                  done = True
            elif (self.board[1] == self.board[7] == self.board[4] and self.board[1] != ' '):
                  self.winner  = self.board[1]
                  done = True
            elif (self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' '):
                  self.winner  = self.board[2]
                  done = True
            elif (self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' '):
                  self.winner  = self.board[0]
                  done = True
            elif (self.board[2] == self.board[4] == self.board[6] and self.board[6] != ' '):
                  self.winner  = self.board[6]
                  done = True
            else:
                  for i in range(9):
                        if self.board[i] == ' ':
                              break
                  else:
                        done = True
            return done

      def show(self):
            # draw the board
            # need to complete the code
            print('\n   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[3], self.board[6]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[1], self.board[4], self.board[7]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[2], self.board[5], self.board[8]))
            print(' +---+---+---+\n')

                  
