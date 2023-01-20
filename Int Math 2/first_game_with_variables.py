import random
import time
enemy_hp = 25
player_hp = 40
items = []
import time
items = []
def first():
  print('You walk into your classroom.')
  time.sleep(1)
  print('You find Sreekar\'s keyboard on the desk.')
  time.sleep(1)
  keyboard = input('Do you pick it up?\n').lower().strip()
  if keyboard == 'yes':
    print('You pick it up.')
    items.append('keyboard')
    time.sleep(1)
    print('You gain +500 Robot, +200 coding knowledge, +80 typing speed, and +200 typing noise.')
  if keyboard == 'no':
    second()
  second()
def second():
  time.sleep(2)
  print('You keep walking and find a sharp sword on the ground.')
  sword = input('Do you pick it up?\n').lower().strip()
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
    fight()
  else:
    print('You die.')
def fight():
  enemy_hp = 25
  player_hp = 40
  while enemy_hp > 0 and player_hp > 0:
    run_or_attack = input('Do you want to attack?\n').lower().strip()
    if run_or_attack == 'no':
      mercy = random.random()
      if mercy > .3:
        print('You walk past the monster. It seems happy that nobody is trying to kill it.')
        break
      else:
        print('You try to walk past, but the monster gets offended by your shirt.')
        time.sleep(1)
        print('The monster attacks you')
        monster_damage = random.randint(5, 12)
        player_hp = player_hp - monster_damage
        time.sleep(1)
        print('You have', player_hp, 'hp left.')
    elif run_or_attack == 'yes':
      print('You attack the monster.')
      random_attack = random.randint(1, 20)
      if random_attack > 8:
        time.sleep(1)
        print('Your attack was successful. ')
        enemy_hp = enemy_hp - random.randint(5, 10)
      else:
        print('Your attack missed.')
      time.sleep(1)
      print('The monster attacks you')
      monster_damage = random.randint(5, 12)
      player_hp = player_hp - monster_damage
      time.sleep(1)
      print('You have', player_hp, 'hp left.')
      if enemy_hp > 0:
        time.sleep(1)
        print('The monster has', enemy_hp, 'hp remaining.')
      else:
        print('The monster has disappeared.')
first()