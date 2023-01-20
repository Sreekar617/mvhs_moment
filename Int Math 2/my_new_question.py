lingling = int(input('How many hours do you practice daily?\n'))
if lingling == 0:
  print('Ling Ling practice 40 hours per day, why cant you do 40 minutes?')
elif lingling <= 3:
  print('Average.')
elif lingling <=6 and lingling >=3:
  print('Are you sure?')
elif lingling >= 7:
  print('Lies.')
elif lingling == 40:
  print('Ling Ling? Is that you?')
else:
  print('Lies.')