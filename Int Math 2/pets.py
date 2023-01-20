pets = int(input('How many pets do you have? (please answer a whole number) '))
if pets > 3:
  print('You\'re crazy! Why do you have', pets, 'pets?')
elif pets == 0:
  print('You should consider getting some pets.')
else:
  print('Amazing! You have', pets, 'pets!')