# variables for the game

has_invite_letter = False


def choose(options):
  print('CHOOSE one of:', options)
  answer = input("> ")
  while answer not in options:
    print('you must pick one of:', options)
    answer = input("> ")
  return answer

def intro():
  print("One bright and sunny day a young adult named Prizma was looking for her cat Butter. Prizma entered a small forest and found a lake. Prizma decided to (a)look for Butter in the lake, or (b) go around the lake and continue looking for Butter in the forest, or (c) turn around and look for Butter in a muddy patch:")
  firstAnswer = choose(['a','b','c'])
  if firstAnswer == "a" :
    print("Cats don't like to swim, silly! The end.")
    the_end()
  elif firstAnswer == "b":
    around_the_lake()
  elif firstAnswer == "c":
    muddy_patch()

def around_the_lake():
  print("You hear what sounds like an animal rustling in the woods up ahead, but you aren't sure what animal it is. Do you (a) run towards the sound, or (b) stay where you are and call Butter's name?")
  secondAnswer = choose(['a','b'])
  if secondAnswer == "a" :
    print("It isn't a cat, it's a bear! It is startled by your sudden appearance and it attacks you. Ouch. The end.")
    the_end()
  else :
    call_butters_name()

def call_butters_name():
  print("You call Butter's name but nothing happens, except the rustling sounds cease. Everything is quiet now. Do you (a) run in the direction the sound used to be coming from, or (b) do you look elsewhere in the woods?")
  thirdAnswer = choose(['a','b'])
  if thirdAnswer == "a" :
    print("You find berries laying on the ground and decied to eat them. At first the berries taste good but they really are poisonous to humans! The end.")
    the_end()
  else :
    print("You see a colorful tree and walk over to it. You realize some people are having a party. As you walk over to everybody you hear a small meowing sound coming from behind the tree. You look where the meowing sound came from and Butter jumped out from behind the tree and into Prizma's arms. Do you (a) try to find a way home or (b) stay at the party?")
    butterAnswer = choose(['a','b'])
    if butterAnswer == "a":
      left_and_right()
    elif butterAnswer == "b":
      the_party()

def the_party():
  global has_invite_letter
  print("You walk over to the entrance but someone asks for the letter you got inviting you there.")
  # check - do you have an invite?
  if has_invite_letter:
    inside_the_party()
  else:
    print("When you say that you were not invited they pull a lever and you fall down a ditch. You walk forward and jump onto a trampoline that bounces you up. When you are back out of the ditch you look around to find your self in a new forest. As you are walking around you find an invitation to the party. Do you (a) pick up the letter or (b) leave it and keep walking?")
    inviteAnswer = choose(['a','b'])
    if inviteAnswer == "a":
      has_invite_letter = True
      # make a change ( set a variable )
      the_party()
    elif inviteAnswer == "b":
      left_and_right()

def inside_the_party():
  print("You pull out the invite you found and hand it to them. The man quickly reads the letter and then says welcome. He opens the gate and you walk in. Do you (a) go over to the snack table or (b) go over to the dance floor?")
  partyTimeAnswer = choose(['a','b'])
  if partyTimeAnswer == "a":
    print("You eat a chocolate cake not knowing that it has peanut butter in it which you are allergic to! The end.")
    the_end()
  elif partyTimeAnswer == "b":
    print("You dance until the song ends and than everyone gathers around the big wooden table. You go over with everyone but one person stops you and asks you your name. You answer Prizma forgetting that you are supposed to be pretending to be someone else. The person pulls out the list of people they invited. I did not invite someone named Prizma they said. Why are you here they asked. Do you (a) say I wanted to meet people or do you (b) say I am the cousin of someone who was invited?")


def left_and_right(): 
  print("You walk forward a little bit and find a trail that goes left and a trail that goes right. Do you (a) go left or (b) go right?")
  trailAnswer = choose(['a','b'])
  if trailAnswer == "a":
    print("You fall off of a cliff. The end.")
    the_end()
  elif trailAnswer == "b":
    print("A huge fox runs over you. The end.")
    the_end()

  
def muddy_patch():
  print("As you start walking towards the muddy patch, it begins to rain very hard. You run to find shelter, and you find a beautiful tent. You hear a meowing sound inside the tent. Do you (a) look inside the tent, or (b) stay where you are and call Butter's name?")
  fourthAnswer = choose(['a','b'])
  if fourthAnswer == "a":
    inside_the_tent()
  elif fourthAnswer == "b":
    call_butters_name()

def inside_the_tent():
  print("The meowing you heard continued coming from behind a red pillow and you go to check it out. You find a cat but it is not Butter. Do you (a) pet the cat or (b) look under the bed that is in the tent or (c) leave the tent and keep looking outside?")
  tentAnswer = choose(['a','b','c'])
  if tentAnswer == "a":
    print("The cat purrs and falls asleep on a button. When the cat pushed down on the button the door to the tent closes. You get locked inside. The end.")
    the_end()
  elif tentAnswer == "b":
    print("You find a hidden staircase that leads underground. You walk down the steps and a huge fan pushes you back upstairs. The trap door shuts and pushes so air at you that pushes you outside the tent and into a muddy patch.")
    muddy_patch()
  elif tentAnswer == "c":
    print("You spot a reindeer that is eating a fish from a stream. The reindeer hears you coming and stops eating to look at you. The reindeer looks at you like its trying to figure out if you want something. The reindeer kicks a nearby bush and then runs off. You stare at the bush it kicked confused and then Butter jumps out of the bush and into your arms with a scared face like a reindeer just kicked his bush when he was trying to steal its fish. The end.")
    the_end()

def the_end():
  print("The end.  Thank you for playing!")
  endAnswer = input("Enter y to play again.")
  if endAnswer == "y":
    intro()
