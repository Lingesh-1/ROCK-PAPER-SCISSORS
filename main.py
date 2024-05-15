#ROCK PAPER or SCISSORS.

import random as r
rps=int(input("Type '0' for Rock, Type '1' for Paper, Type '2' for Scissors:\n"))
l=["Rock","Paper","Scissors"]
print("You chossed:",l[rps])


if rps==0:
    print('''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                            ''')


elif rps==1:
    print('''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88 ''')


elif rps==2:
    print('''
    emmmmmm~~~~~~~~~~~~~~~~~~~~~~~~~.
    """"""|_____                    )
                """""""""--------"""''')
else:
    print("INVALID NUMBER!!!")


print("\n")
v= r.randint(0,len(l)-1)
print("Computer's chossed:",l[v])
if v==0:
    print('''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                            ''')
    if rps==2:
        print("You loss the game!!!")
    elif rps==1:
        print("You Won the Game!!!")
    elif rps==0:
        print("Draw match!!!")

elif v==1:
    print('''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88 ''')
    if rps==2:
        print("You Won the Game!!!")
    elif rps==1:
        print("Draw Match")
    elif rps==0:
        print("You Loss the Game!!!")
elif v==2:
    print('''
    emmmmmm~~~~~~~~~~~~~~~~~~~~~~~~~.
    """"""|_____                    )
                """""""""--------"""''')
    if rps==2:
        print("Draw match!!!")
    elif rps==1:
        
        print("You loss the game!!!")
    elif rps==0:
        print("You Won the game!!!")
