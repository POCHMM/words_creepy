palabra = input("Que Palabra Quieres Aprender: ")

meme_dict = ("cringe":"pena ajena", 
  "gg": "good game",
  "npc": "no playable character",
  "BRB": "Be Right Back",
  "IDK": "I Dont Know",
  "zzz": "Dormido", 
  "FPS": "Fotogramas Por Segundo o First Person Shooter",
  "XP": "Experience Points",
  "Noob": "Novato",
  "Hitbox": "Caja De Daño")

if palabra in meme_dict.keys():
  print(meme_dict[palabra])
else:
  print("Esa Palabra No La Tenemos")
