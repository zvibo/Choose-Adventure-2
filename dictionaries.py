# This is leftover junk from a previous experiment
# It has nothing to do with our choose your own adventure

favorites = { 
  "Aria":{
    "color":"yellow",
    "food":"raspberries"
  },
  "David":{
    "color":"blue",
    "food":"soda"
  },
  "Eve":{"color":"red","food":"chocolate"},
  "Keiko":{
    "color":"black",
    "food":"dog treats"
  }
}

for person in favorites:
  print(person + " loves the color " + 
    favorites[person]["color"] + ".")
  print(person + " loves to eat " + 
    favorites[person]["food"] + ".")