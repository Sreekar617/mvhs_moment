sports = input('Do you do sports outside of school?\n').lower().strip()
if sports == 'yes':
  sport = input('What sports do you play?\n').lower().strip()
  if sport == 'volleyball':
    print('I know a lot of people who play volleyball')
  elif sport == 'hockey':
    print('Don\'t hurt youself on the ice')
  else:
    print('Amazing! I like', sport, 'too!')
if sports == 'no':
  outside = input('What do you do after school?\n').lower().strip()
  if outside == 'nothing':
    print('You should go outside more.')
  elif outside == 'homework':
    print('Get that A!')
  else:
    print('After school activities are always fun.')