swim = input('Do you like to swim in the summer?\n').lower().strip()
if swim == 'yes':
  stroke = input('What is your favorite swimming stroke?\n').lower().strip()
  if stroke == 'backstroke':
    print('I hate when water gets in my ear.')
  elif stroke == 'front crawl':
    print('That\'s a pretty fast stroke')
  else:
    print('Amazing! I like', stroke, 'too!')
if swim == 'no':
  outside = input('What do you like to do outside in the summer?\n').lower().strip()
  if outside == 'nothing':
    print('You should go outside more.')
  elif outside == 'riding bike':
    print('Biking is always fun in the summer')
  else:
    print('Going outside in the summer is always fun.')