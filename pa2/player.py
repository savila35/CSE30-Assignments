# author: Sebastian Avila
# date: February 7, 2023
# file: player.py is a python program that contains a player class for a tictactoe game. There are also two subclasses of player: AI and MiniMax. 
# input: user name, user game sign, and user responses (strings)
# output: input prompts and game moves

from random import choice
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X

      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name

      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
            while True: 
                  try:
                        cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
                        if cell in valid_choices :
                              if board.isempty(cell):
                                    board.set(cell, self.sign)
                                    break
                              else:
                                    raise
                        else:
                              raise
                  except:
                        print('You did not choose correctly.')
                        
class AI(Player):
      def __init__(self, name, sign, board):
           self.name = name
           self.sign = sign
           self.board = board

      def choose(self,board):
            valid_choices = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
            possible_moves = [i for i in valid_choices if self.board.board[valid_choices.index(i)]== ' ']
            cell = choice(possible_moves)
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            board.set(cell,self.sign)
class SmartAI(AI):
      def choose(self, board):
            all_cells = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
            if board.board[4] == self.sign:
                  pass

class MiniMax(Player):
      def __init__(self, name, sign, board):
           self.name = name
           self.sign = sign
           self.board = board
           self.opp_sign = 'O' if self.sign == 'X' else 'X'

      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)

      def minimax(self, board, self_player, start):
            max_score = float('-inf')
            min_score = float('inf')
            all_cells = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
            move = ''
            # check the base conditions   
            if board.isdone():
                  # self is a winner
                  if board.get_winner() == self.sign:
                        return 1
                  # is a tie
                  elif board.get_winner() == '':
                        return 0
                  # self is a looser (opponent is a winner)
                  else:
                        return -1
            else:
                  if self_player:
                        for x in all_cells:
                              if board.isempty(x):
                                    board.set(x, self.sign)
                                    score = MiniMax.minimax(self, self.board, False, False)
                                    move = x if score > max_score else move 
                                    max_score = max(max_score, score)
                                    board.set(x,' ')
                        return move if start else max_score
                  else:
                        for x in all_cells:
                              if board.isempty(x):
                                    board.set(x,self.opp_sign)
                                    score = MiniMax.minimax(self, self.board, True, False)
                                    min_score = min(min_score, score)
                                    board.set(x,' ')              
                        return min_score
                        
                  