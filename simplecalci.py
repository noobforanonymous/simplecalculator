
green = '\033[1;92m'
red = '\033[31m'
blue = '\033[34m'
clear = '\033[0m'
bold = '\033[01m'

print(green + """
 _____ _______   _    _          _____ _  __ _____ 
|  __ \__   __| | |  | |   /\   / ____| |/ // ____|
| |__) | | |    | |__| |  /  \ | |    | ' /| (___  
|  _  /  | |    |  __  | / /\ \| |    |  <  \___ \ 
| | \ \  | |    | |  | |/ ____ \ |____| . \ ____) |
|_|  \_\ |_|    |_|  |_/_/    \_\_____|_|\_\_____/ 
""" + green)
print(red + bold + "   <====YOUTUBE CHANNEL NAME : RTHACKS====> \n" + clear)
print(blue + bold + " <=========https://dev-regaanthamimprogramming.pantheonsite.io/=======> \n" + clear)


rthacks = input("YOUR EXPRESSION : ")
print("ANSWER : " , eval(rthacks))
