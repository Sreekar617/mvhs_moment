cart = []
while True:
  add = input('What do you want to add to your grocery cart?\n')
  if add == 'nothing':
    break
  else:
    print('You add', add, 'to your cart,')
    cart.append(add)
print(cart)