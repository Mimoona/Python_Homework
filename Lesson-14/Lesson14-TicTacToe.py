# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:04:37 2020

@author:
"""
import random
EMPTY_SLOT = "-"
X_PLAYER = "X"
O_PLAYER = "0"
TIE = "tie"

WIN_COMBINATION_INDICES = [
  # Complete row
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  # Complete column
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  # Complete diagonal
  [0, 4, 8],
  [2, 4, 6]
]


def initialize_board():
  board = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
  return board


def display_board(board):
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")
  
  
def handle_turn(player, board):
  print(f"{player}, it's your turn.")

  # TODO Ask player to input a position (1-9). Ask while the position is not valid (check using valid_position)
  position = input('Enter the position: ') 
  
  check_input_valid = False
  
  # keep executing until get the valid input
  while check_input_valid == False:  
      check_input_valid = valid_position(position,board)
      if check_input_valid == False:
          
          # Take input and check again if its correct.Execute while again
          position = input('Enter the position: ')
      else:
          #Get the index on board because valid_position just return True or False
          position = int(position)-1
    
  #update the board
  board[position] = player
  return board


# Checks the input is valid (user entered only one number, position is not filled)
def valid_position(position, board):
  valid = False
  # List contains string because we are comparing input which is by default str type
  valid_list = ['1','2','3','4','5','6','7','8','9']
    
  # TODO Check if the position is a number between 1 and 9 AND if it is empty (EMPTY_SLOT)
 
  if position in valid_list:
      # Get the index to check if slot is empty on board
      position = int(position)-1
      if board[position] == EMPTY_SLOT:
        valid = True
      else:
        print('Sorry, your slot is already filled')
  else:
      print('Sorry, You have made a wrong input')
  return valid
  
  
     
def switch_player(player):
  # TODO Switch the player: X --> 0 or 0 --> X
  if player == X_PLAYER:
      player = O_PLAYER
  else:
      player = X_PLAYER   
  return player


def check_for_winner(board,player):

  winner = None
  filled_slots = 0
  for i in board:
    if i!= EMPTY_SLOT:
        filled_slots+=1
        
  # TODO Check if any of the players got a win combination
     
  # Hint: loop over WIN_COMBINATION_INDICES to check if one of the combination is X-X-X or O-O-O
  
  for each_list in WIN_COMBINATION_INDICES:
    i1 = each_list[0]
    i2 = each_list[1]
    i3 = each_list[2]
    if board[i1]==player and board[i2]==player and board[i3]==player:
        winner = player
        #break
    
  if filled_slots==9 and winner==None:
    winner = TIE
  return winner
 

def random_turn():
  rand_num = random.randint(0,1)
  
  if rand_num == 0:
      player = X_PLAYER
  else:
      player = O_PLAYER
  return player


def tic_tac_toe():
  winner = None
  game_still_going = True
  #player = X_PLAYER  # X will start. TODO (optional): select who starts randomly --> do this in a separate function
  player = random_turn()

# Initialize board
  board = initialize_board()

  # TODO run this while the game is still going
  while game_still_going:
      
      # Display board
      display_board(board)

      # Ask the player for a valid position and write it on the board
      board = handle_turn(player, board)
      
      # Check if there is a winner already
      winner = check_for_winner(board,player)
      if winner == player:
          display_board(board)
          print(f"Congratulations Player {winner}, You won!!!")
          game_still_going = False

      elif winner == TIE:
          display_board(board)
          print("Game is a Tie")
          game_still_going = False

      # TODO stop the game if there is a winner, otherwise switch the player
      player = switch_player(player)
      
  #display_board(board)
  print("THE END")

# Start game
tic_tac_toe()



