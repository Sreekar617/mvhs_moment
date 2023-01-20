while True:
  fishing = input('Do you like to fish?\n').lower().strip()
  if fishing == 'yes':
    print('I like to fish too')
    break
  elif fishing == 'no':
    print('There are still many fun activities outside that aren\'t fishing.')
    break
  else:
    print('Why is this question so hard to answer? Say yes or no!\n')