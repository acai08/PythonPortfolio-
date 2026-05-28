#Annie
#Pokemon
#Create a Pokemon game.

import random

name = "Squirtle"
level = 0
day = 1
boss_defeated = 0

def stage1():
   print((r"              _,........__\n"))
   print((r"           ,-'            \"`-.\n"))
   print((r"         ,'                   `-.\n"))
   print((r"       ,'                        \\\n"))
   print((r"     ,'                           .\n"))
   print((r"     .'\\               ,\"\".       `\n"))
   print((r"    ._.'|             / |  `       \\\n"))
   print((r"    |   |            `-.'  ||       `.\n"))
   print((r"    |   |            '-._,'||       | \\\n"))
   print((r"    .`.,'             `..,'.'       , |`-.\n"))
   print((r"    l                       .'`.  _/  |   `.\n"))
   print((r"    `-.._'-   ,          _ _'   -\" \\  .     `\n"))
   print(("`.\"\"\"\"\"'-.`-...,---------','         `. `....__.\n"))
   print((".'        `\"-..___      __,'\\          \\  \\     \\\n"))
   print(("\\_ .          |   `\"\"\"\"'    `.           . \\     \\\n"))
   print((r" `.          |              `.          |  .     L\n"))
   print((r"   `.        |`--...________.'.        j   |     |\n"))
   print((r"     `._    .'      |          `.     .|   ,     |\n"))
   print((r"        `--,\\       .            `7\"\"' |  ,      |\n"))
   print((r"           ` `      `            /     |  |      |    _,-'\"\"\"`-.\n"))
   print((r"            \\ `.     .          /      |  '      |  ,'          `.\n"))
   print((r"             \\  v.__  .        '       .   \\    /| /              \\\n"))
   print((r"              \\/    `\"\"\\\"\"\"\"\"\"\"`.       \\   \\  /.''                |\n"))
   print((r"               `        .        `._ ___,j.  `/ .-       ,---.     |\n"))
   print((r"               ,`-.      \\         .\"     `.  |/        j     `    |\n"))
   print((r"              /    `.     \\       /         \\ /         |     /    j\n"))
   print((r"             |       `-.   7-.._ .          |\"          '         /\n"))
   print((r"             |          `./_    `|          |            .     _,'\n"))
   print((r"             `.           / `----|          |-............`---'\n"))
   print((r"               \\          \\      |          |\n"))
   print((r"              ,'           )     `.         |\n"))
   print((r"               7____,,..--'      /          |\n"))
   print((r"                                 `---.__,--.'mh\n"))

def stage2():
   print((r"    __                                _.--'\"7\n"))
   print((r"   `. `--._                        ,-'_,-  ,'\n"))
   print((r"    ,'  `-.`-.                   /' .'    ,|\n"))
   print((r"    `.     `. `-     __...___   /  /     - j\n"))
   print((r"      `.     `  `.-\"\"        \" .  /       /\n"))
   print((r"        \\     /                ` /       /\n"))
   print((r"         \\   /                         ,'\n"))
   print((r"         '._'_               ,-'       |\n"))
   print((r"            | \\            ,|  |   ...-'\n"))
   print((r"            || `         ,|_|  |   | `             _..__\n"))
   print((r"           /|| |          | |  |   |  \\  _,_    .-\"     `-.\n"))
   print((r"          | '.-'          |_|_,' __!  | /|  |  /           \\\n"))
   print((r"  ,-...___ .=                  ._..'  /`.| ,`,.      _,.._ |\n"))
   print((r" |   |,.. \\     '  `'        ____,  ,' `--','  |    /      |\n"))
   print((r",`-..'  _)  .`-..___,---'_...._/  .'      '-...'   |      /\n"))
   print(("'.__' \"\"'      `.,------'\"'      ,/            ,     `.._.' `.\n"))
   print((r" `.             | `--........,-'.            .         \\     \\\n"))
   print((r"   `-.          .   '.,--\"\"     |           ,'\\        |      .\n"))
   print((r"      `.       /     |          L          ,\\  .       |  .,---.\n"))
   print((r"        `._   '      |           \\        /  .  L      | /   __ `.\n"))
   print((r"           `-.       |            `._   ,    l   .    j |   '  `. .\n"))
   print((r"             |       |               `\"' |  .    |   /  '      .' |\n"))
   print((r"             |       |                   j  |    |  /  , `.__,'   |\n"))
   print((r"             `.      L                 _.   `    j ,'-'           |\n"))
   print((r"              |`\"---..\\._______,...,--' |   |   /|'      /        j\n"))
   print((r"              '       |                 |   .  / |      '        /\n"))
   print((r"               .      .              ____L   \\'  j    -',       /\n"))
   print((r"              / `.     .          _,\"     \\   | /  ,-','      ,'\n"))
   print((r"             /    `.  ,'`-._     /         \\  i'.,'_,'      .'\n"))
   print((r"            .       `.      `-..'             |_,-'      _.'\n"))
   print((r"            |         `._      |            ''/      _,-'\n"))
   print((r"            |            '-..._\\             `__,.--'\n"))
   print((r"           ,'           ,' `-.._`.            .\n"))
   print((r"          `.    __      |       \"'`.          |\n"))
   print((r"            `-\"'  `\"\"\"\"'            7         `.\n"))
   print((r"                                   `---'--.,'\"`' mh\n"))

def stage3():
   print((r"                      _\n"))
   print((r"           _,..-\"\"\"--' `,.-\".\n"))
   print((r"         ,'      __.. --',  |\n"))
   print((r"       _/   _.-\"' |    .' | |       ____\n"))
   print((r" ,.-\"\"'    `-\"+.._|     `.' | `-..,',--.`.\n"))
   print((r"|   ,.                      '    j 7    l \\__\n"))
   print((r"|.-'                            /| |    j||  .\n"))
   print((r"`.                   |         / L`.`\"\"','|\\  \\\n"))
   print((r"  `.,----..._       ,'`\"'-.  ,'   \\ `\"\"'  | |  l\n"))
   print((r"    Y        `-----'       v'    ,'`,.__..' |   .\n"))
   print((r"     `.                   /     /   /     `.|   |\n"))
   print((r"       `.                /     l   j       ,^.  |L\n"))
   print((r"         `._            L       +. |._   .' \\|  | \\\n"))
   print((r"           .`--...__,..-'\"\"'-._  l L  \"\"\"    |  |  \\\n"))
   print((r"         .'  ,`-......L_       \\  \\ \\     _.'  ,'.  l\n"))
   print((r"      ,-\"`. / ,-.---.'  `.      \\  L..--\"'  _.-^.|   l\n"))
   print((r".-\"\".'\"`.  Y  `._'   '    `.     | | _,.--'\"     |   |\n"))
   print((r" `._'   |  |,-'|      l     `.   | |\"..          |   l\n"))
   print((r" ,'.    |  |`._'      |      `.  | |_,...---\"\"\"\"\"`    L\n"))
   print((r"/   |   j _|-' `.     L       | j ,|              |   |\n"))
   print(("`--,\"._,-+' /`---^..../._____,.L',' `.             |\\  |\n"))
   print((r"  |,'      L                   |     `-.          | \\j\n"))
   print((r"           .                    \\       `,        |  |\n"))
   print((r"            \\                __`.Y._      -.     j   |\n"))
   print((r"             \\           _.,'       `._     \\    |  j\n"))
   print((r"             ,-\"`-----\"\"\"\"'           |`.    \\  7   |\n"))
   print((r"            /  `.        '            |  \\    \\ /   |\n"))
   print((r"           |     `      /             |   \\    Y    |\n"))
   print((r"           |      \\    .             ,'    |   L_.-')\n"))
   print((r"            L      `.  |            /      ]     _.-^._\n"))
   print((r"             \\   ,'  `-7         ,-'      / |  ,'      `-._\n"))
   print((r"            _,`._       `.   _,-'        ,',^.-            `.\n"))
   print((r"         ,-'     v....  _.`\"',          _:'--....._______,.-'\n"))
   print((r"       ._______./     /',,-'\"'`'--.  ,-'  `.\n"))
   print((r"                \"\"\"\"\"`.,'         _\\`----...' mh\n"))
   print((r"                       --------\"\"'\n"))
   print(("\n"))
   print(("\n"))

def main():
   global day
   global boss_defeated
   print("Welcome to Pokemon!")
   print(f"Your Pokemon is {name}")
   while True:
       print(f"day {day}")
       menu = input("What would you like to do to your pokemon? (train, rest, exit, boss battle): ")
       if menu == "train":
           train()
           battle()
           evolve()
           info()
       elif menu == "rest":
           print("Your pokemon is resting")
       elif menu == "boss battle":
           final_boss()
           if boss_defeated == 1:
               break
       else:
           break
       day = day + 1

def evolve():
   global name
   if level < 10:
       name = name
   elif level >= 10 and level <= 19:
       print("Your Pokemon evolved!")
       name = "Wartortle"
   else:
       print("Your Pokemon evolved!")
       name = "Blastoise"

def train():
   global level
   level = level + 1
   print(f"{name} energetically played with water!")

def battle():
   global level
   combat = input("Would you like to go into battle?: ")
   if combat == "yes":
       fight = random.randint(1, 2)
       if fight == 1:
           print("You Win! Pokemon levels up by 2.")
           level = level + 2
       else:
           print("You Lose!")

def final_boss():
   global level
   global boss_defeated
   while True:
       boss = input("Would you like to fight the final boss?: ")
       if boss == "yes":
           if level <= 10:
               chance = input("if final boss is attempted at low level, there is a high chance of losing. Continue?: ")
               if chance == "yes":
                   final = random.randint(1, 10)
                   if final <= 9:
                       print("YOU LOSE")
                       return main
                   else:
                       print("YOU WIN")
                       boss_defeated = 1
                       break
               else:
                   return main
           elif level <= 20:
               chance = input("if final boss is attempted at low level, there is a high chance of losing. Continue?: ")
               if chance == "yes":
                   final = random.randint(1, 10)
                   if final <= 7:
                       print("YOU LOSE")
                       return main
                   else:
                       print("YOU WIN")
                       boss_defeated = 1
                       break
               else:
                   return main
           else:
               final = random.randint(1, 10)
               if final <= 5:
                   print("YOU LOSE")
                   return main
               else:
                   print("YOU WIN")
                   boss_defeated = 1
                   break
       else:
           return main

def info():
   global level
   global name
   print(f"{name} info:")
   print(f"level: {level}")
   if name == "Squirtle":
       stage1()
   elif name == "Wartortle":
       stage2()
   else:
       stage3()

main()
