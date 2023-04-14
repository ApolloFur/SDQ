import random
import character
import rooms
import items

Player = character.Player("placeholder",0,[0,0],100,100,6,6,5,6,6)
#generate default player inventory
Player.inv = {}
Player.inv["Broadword"] = items.Weapon("Broadword",1,[3,6],2)
Player.inv["Crossbow"] = items.Weapon("Crossbow",1,[4,4],10)
Player.inv["HPotion"] = items.Consumable("HPotion",5,0)
Player.inv["Mpotion"] = items.Consumable("MPotion",5,1)
Player.inv["CONPotion"] = items.Consumable("CONPotion",1,2)

#generate map
ROOMS = {}
ROOMS["West Wall"] = rooms.Room("West Wall",[-1, 3],[-11,5],"A large wall that sprawls for miles stands beore you. It's crooked, mossy bricks barely held together feel like they're going to break. Beyond the wall you see what looks like a large castle, something that once might've belonged to a king, but now lays decrepit and dead. But through it you see horrible new life. A large beam of light rises from the center of it all, peircing the heavens with it's demonic glow. This is why you have been sent here with your two fellow mercenaries. Within lies a lich king, a horrible monstrosity capable of reanimating the dead. The king from yonder kingdom is afraid of the lich king's presence, and has hired you to exterminate him with the aid of two other swords-for-hire. You've better get to work.")
ROOMS["North Wall"] = rooms.Room("North Wall",[-5,5],[-2,2],"The wall makes a sharp 90 degree turn and you see a large pile of rubble. At the top, a single door that you couldn't hope of reaching this low.")
ROOMS["Courtyard 1"] = rooms.Room("Courtyard 1",[-12,10],[-5,5],"A large field of dead grass stand before you, as undead creatures patrol around the castle grounds. A tree stand in the middle, along with other small peices of dead shrubbery.")
ROOMS["Courtyard 2"] = rooms.Room("Courtyard 2",[-6,8],[-6,8],"The courtyard continues even further. The dead grass is now punctuated by large rocks jutting out of the lifeless ground.")
ROOMS["Prison Cell 1"] = rooms.Room("Prison Cell 1",[-1,2],[-2,2],"The inside of this prison cell is damp. Puddles strewn across the floor wet your boots. You hope you havn't cause a disease from this disgusting musk.")
ROOMS["Prison Cell 2"] = rooms.Room("Prison Cell 2",[-1,2],[-2,2],"The inside of this prison cell contains little more than bundles of hay on the floor. A chain swings from the roof, but little lays within.")
ROOMS["Prison Cell 3"] = rooms.Room("Prison Cell 3",[-1,2],[-2,2],"There's little within this cell. Only some spiderwebs and the standard cracked bricks that make up this castle.")
ROOMS["Prison Cell 4"] = rooms.Room("Prison Cell 4",[-1,2],[-2,2],"This cell hides a small nest of rats that scitter across the floor as you enter. Their squeaks provide a welcomed sound of life.")
ROOMS["Prison Cell 5"] = rooms.Room("Prison Cell 5",[-1,2],[-2,2],"A skeleton hides within this cell, surprisingly unanimated. A contrast than most other skeeltons here. Perhaps he did something that warranted he not be reanimated?")
ROOMS["Prison Cell 6"] = rooms.Room("Prison Cell 6",[-1,2],[-2,2],"A gaping hole has burned a permanent mark on this prison cell. Sadly, the hole is too small to squeeze through, but something tells you that you didn't want to see what's behind in the first place.")
ROOMS["Prison Hallway 1"] = rooms.Room("Prison Hallway 1",[-2,2],[-9,3],"A dank hallway connect the prison cells among each other, allowing each to be easily accessed.")
ROOMS["Prison Hallway 2"] = rooms.Room("Prison Hallway 2")