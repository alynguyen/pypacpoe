print('-----------------------')
print("Let's play Py-Pac-Poe!")
print('-----------------------')

#Global Variables
board = {}
turn = 'X'

def init_game():
  global board, turn
  board = {
    'a1': None, 'b1': None, 'c1': None,
    'a2': None, 'b2': None, 'c2': None,
    'a3': None, 'b3': None, 'c3': None,
  }
  turn = 'X'

def render():
  global board
  print('    A     B     C')
  print(f"1)  {board['a1'] or ' '}  |  {board['b1'] or ' '}  |  {board['c1'] or ' '}")
  print('   ---------------')
  print(f"2)  {board['a2'] or ' '}  |  {board['b2'] or ' '}  |  {board['c2'] or ' '}")
  print('   ---------------')
  print(f"3)  {board['a3'] or ' '}  |  {board['b3'] or ' '}  |  {board['c3'] or ' '}")

def get_move():
  winner = None
  global board, turn
  while winner is None:
    if turn == 'X':
      move = input('Enter move for X: ').lower()
      board[move] = turn
      turn = 'O'
      render()
    if turn == 'O':
      move = input('Enter move for 0: ').lower()
      board[move] = turn
      turn = 'X'
      render()


init_game()
render()
get_move()

