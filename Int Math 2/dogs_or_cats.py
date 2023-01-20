pet = input('What do you like better as a pet, dogs or cats?\n').strip().lower()
if pet == 'dogs' or pet == 'dog':
  breed = input('What breed of dog do you like?\n').lower().strip()
  if breed == 'corgi':
    print('I heard that Mr. Hieb heard that they sleep a lot')
  elif breed == 'poodle' or breed == 'pomeranian':
    print('floof')
  else:
    print('Wow! I like', breed, 'too!')
else:
  print('mewo (omg future reference?! omg sreekars program reference?!)')