import time
items = []
def first():
  print('You walk into your classroom.')
  time.sleep(1)
  print('You find Sreekar\'s keyboard on the desk.')
  keyboard = input('Do you pick it up?\n').lower().strip()
  if keyboard == 'yes':
    print('You pick it up.')
    items.append('keyboard')
    time.sleep(1)
    print('You gain +500 Robot, +200 coding knowledge, +80 typing speed, and +20000000 typing noise.')
  if keyboard == 'no':
    second()
  second()
def second():
  print('You keep walking and find a sharp sword on the ground.')
  sword = input('Do you pick it up?')
  if sword == 'yes':
    print('You pick it up')
    items.append('sword')
    time.sleep(1)
    print('It\'s really sharp.')
    monster()
  elif sword == 'no':
    monster()
  monster()
def monster():
  print('A monster is blocking your path!')
  weapons = input('What do you want to attack with?\n').lower().strip()
  if weapons == 'keyboard':
    print('You pull out the keyboard and feel robot powers flowing through your veins.')
    time.sleep(3)
    print('You start typing at 300wpm.')
    time.sleep(3)
    print('The monster seems bothered by the noise you\'re making.')
    time.sleep(3)
    print('Within 3 seconds, you have hacked the fabric of the universe and removed all monsters. You teleport to the end and win.\n\n')
    time.sleep(5)
    first()
  elif weapons == 'sword':
    print('The sword crumbles to the monsters tough skin. You get eaten by the monster and die.')
    first()
  else:
    print('You die.')
first()