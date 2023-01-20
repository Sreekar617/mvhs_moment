import time
egg = input('You find an egg on the ground. Do you eat or pass by?\n').lower().strip()
if egg == 'eat':
  print('You pick up the egg')
  time.sleep(2)
  print('You put it on the frying pan')
  time.sleep(2)
  print('You put it on a plate and grab your fork')
  time.sleep(2)
  print('You put it in your mouth')
  time.sleep(4)
  print('You die instantly. The egg was poisoned.')
elif egg == 'pass by':
  print('You walk past the egg')
  time.sleep(4)
  print('You get run over by a dump truck that swerved to avoid the egg.')