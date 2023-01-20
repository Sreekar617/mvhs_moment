strong = int(input('How many days do you exercise per week?\n'))
if strong == 0:
  print('You should probably exercise more')
elif strong <= 3:
  print('You exercise sometimes')
elif strong <=6 and strong >=3:
  print('You get good exercise')
elif strong == 7:
  print('You are very athletic')
else:
  print('Lies.')