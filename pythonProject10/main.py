import time
import sys
from timeit import default_timer as timer
from Library import intro
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.007)
#spaceship art
#def nextscreen(ok):

# start = timer()
# end = timer()
# time = int(end - start)
# delay_delay_print = (time)
# or
# delay_print(f"{time:.2f}s")
import os
def death():
    delay_print("You Died! Game Over")
    quit()


spaceship ='''
                        `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \.'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \.
                               `._________`-.   `.   `.___
                                                  `------'`

 **       **   *******   *******   **       *******   **       ** ****     ** ********   
/**      /**  **/////** /**////** /**      /**////** /**      /**/**/**   /** /**/////    
/**   *  /** **     //**/**   /** /**      /**    /**/**      /**/**//**  /** /**    
/**  *** /**/**      /**/*******  /**      /**    /**/**      /**/** //** /** /*******
/** **/**/**/**      /**/**///**  /**      /**    /**/**      /**/**  //**/** /**////   **
/**** //****//**     ** /**  //** /**      /**    ** /**      /**/**   //**** /**      // 
/**/   ///** //*******  /**   //**/********/*******  /********/**/**    //*** /******** **
//       //   ///////   //     // //////// ///////   //////// // //      ///  //////// // 

'''

#Basic Instruction for dialogue/menu
delay_print("Type 'ok' to move forward \n")
next_screen = input("Type Here: ")
os.system("clear")

#Title Screen
while next_screen != "ok":
    delay_print("Fine then, I didn't want to play anyways. Hmph.\n")
    next_screen = input("Type Here: ")
    os.system("clear")
else:
    delay_print("Greetings Traveler, welcome to...")
time.sleep(2)
delay_print(spaceship)
delay_print("A SPACE VOYAGE\n")


#Main Menu
next_screen = input("Type Here: ")
while next_screen != "ok":
    delay_print("Hey Numbnuts! you're supposed to type 'ok', get it right!\n")
    next_screen = input("Type Here: ")
    os.system("clear")
else:
    delay_print("MENU:\n")
    print()
    delay_print("1. -New Game-\n")
choice = input("Type Number Here: ")
os.system("clear")
# If not 1 or 2
while choice != str(1):
    delay_print("There are only two numbers on screen man, come on\n")
    next_screen = input("Type Here: ")
    while next_screen != "ok":
        delay_print("Hey Numbnuts! you're supposed to type 'ok', get it right!\n")
        next_screen = input("Type Here: ")
    delay_print("MENU:\n")
    print()
    delay_print("1. -New Game-\n")
    delay_print("-High Score-\n")
    choice = input("Type Number Here: ")
    while choice != "1":
        delay_print("There's only one number on screen man\n")
        choice = input("Type Number Here: ")
    os.system("clear")

# NEW GAME
if choice == str(1):
    start = timer()
    intro()

