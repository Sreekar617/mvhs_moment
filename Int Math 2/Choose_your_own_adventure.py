x=5
while True:
  choice = input('Do you want to go upstairs, into the bedroom, or into the kitchen?\n').lower().strip()
  if choice == 'kitchen' or choice == 'bedroom':
    print('The place is full of hungry monsters. You die.')
    x=x-1
    if x == 0:
      print('Game Over')
      break
  elif choice == 'upstairs':
    print('You found the treasure!')
    break