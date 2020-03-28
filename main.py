print("One bright and sunny day a young adult named Prizma was looking for her cat Butter. Prizma entered a small forest and found a lake. Prizma decided to (a)look for Butter in the lake, or (b) go around the lake and continue looking for Butter in the forest, or (c) turn around and look for Butter in a muddy patch:")
firstAnswer = input("Enter a, b, or c: ")
while firstAnswer != ("a","b","c") :
  if firstAnswer == "a" :
    print("Cats don't like to swim, silly! The end.")
    break

  elif firstAnswer == "b" :
    print("You hear what sounds like an animal rustling in the woods up ahead, but you aren't sure what animal it is. Do you (a) run towards the sound, or (b) stay where you are and call Butter's name?")
    secondAnswer = input("Enter a or b: ")
    if secondAnswer == "a" :
      print("It isn't a cat, it's a bear! It is startled by your sudden appearance and it attacks you. Ouch. The end.")
    else :
      print("You call Butter's name but nothing happens, except the rustling sounds cease. Everything is quiet now. Do you (a) run in the direction the sound used to be coming from, or (b) do you look elsewhere in the woods?")
      thirdAnswer = input("Enter a or b:")
      if thirdAnswer == "a" :
        print("You find berries laying on the ground and decied to eat them. At first the berries tast good but they really are poisnous to humans! The end.")
      else :
        print("You see a colorful tree and walk over to it. You realize some people are having a party. As you walk over to everybody you hear a small meowing sound coming from behind the tree. You look were the meowing sound came from and Butter jumped out from behind the tree and into Prizma's arms. Happy ending.")
    break
   
  elif firstAnswer == "c" :
    print("As you start walking towards the muddy patch, it begins to rain very hard. You run to find shelter, and you find a beautiful tent. You hear a meowing sound inside the tent. Do you (a) look inside the tent, or (b) stay where you are and call Butter's name?")
    break

  else :
    firstAnswer = input("You need to enter a, b, or c: ")