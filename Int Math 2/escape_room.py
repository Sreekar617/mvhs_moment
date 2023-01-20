import time
def living_room():
  print('You are in the living room')
  next = input('Where would you like to go next?\n(Bedroom, Den, Kitchen, Bathroom, Closet)').lower().strip()
  if next == 'bedroom':
    bedroom()
  if next == 'den':
    den()
  if next == 'kitchen':
    kitchen()
  if next == 'bathroom':
    bathroom()
  if next == 'closet':
    closet()
  else:
    print('That\'s not an option')
    living_room()
def bedroom():
  print('You move to the bedroom.\n There\'s nothing here except a bed.')
  time.sleep(1)
  next = input('Where would you like to go next?\n(Living Room)\n').lower().strip()
  if next == 'living room':
    living_room()
  else:
    print('That\'s not a valid answer.')
    bedroom()
def den():
  print('You move to the den.\n There\'s nothing here except an old sofa.')
  time.sleep(1)
  next = input('Where would you like to go next?\n(Living Room, Kitchen)\n').lower().strip()
  if next == 'living room':
    living_room()
  if next == 'kitchen':
    kitchen()
  else:
    print('That\'s not an option.')
    den()
def kitchen():
  print('You move to the kitchen.\n There\'s nothing here except some old pans.')
  time.sleep(1)
  next = input('Where would you like to go next?\n(Escape, Living Room, )\n').lower().strip()
  if next == 'living room':
    living_room()
  if next == 'kitchen':
      kitchen()
  if next == 'escape':
    escape()
  else:
    print('That\'s not an option.')
    kitchen()
def bathroom():
  print('You move to the bathroom.\n There\'s nothing here except a rusted toilet.')
  time.sleep(1)
  next = input('Where would you like to go next?\n(Living Room)\n').lower().strip()
  if next == 'living room':
    living_room()
  else:
    print('That\'s not an option.')
    bathroom()
def closet():
  print('You move to the closet. The closet is filled to the top with eggs.')
  time.sleep(1)
  print('The eggs fall on your head and you die.')
  print(list(range(0, 500000000, 1)))
def escape():
  print('You escaped!')
living_room()