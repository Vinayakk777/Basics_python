import time
import sys
import random

# --- Helper function for dramatic text ---
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# --- Main Game ---
def treasure_island():
    print(r'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ___           ___           ___           ___                   
             /\  \         /\  \         /\__\         /\__\                  
            /::\  \       /::\  \       /:/  /        /::|  |                 
           /:/\:\  \     /:/\:\  \     /:/__/        /:|:|  |                 
          /::\~\:\  \   /::\~\:\  \   /::\__\____   /:/|:|  |__               
         /:/\:\ \:\__\ /:/\:\ \:\__\ /:/\:::::\__\ /:/ |:| /\__\              
         \/__\:\/:/  / \/__\:\/:/  / \/_|:|~~|~    \/__|:|/:/  /              
              \::/  /       \::/  /     |:|  |         |:/:/  /               
               \/__/         \/__/      |:|  |         |::/  /                
                                        |:|  |         |:/  /                 
                                        |:|  |         |/__/                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
    slow_print("Welcome to Treasure Island, adventurer!")
    slow_print("Your mission is to find the lost pirate's treasure. 🏴‍☠️\n")

    # --- First Choice ---
    first = input("You're at a crossroad. Do you go Left or Right? ").strip().lower()

    if first == "right":
        print(r'''
             .-=========-.
             \'-=======-'/ 
             _|   .=.   |_
            ((|  {{1}}  |))
             \|   /|\   |/
              \__ '`' __/
                _`) (`_
              _/_______\_
             /___________\
        ''')
        slow_print("⚡ Oh no! Sonic zoomed past and grabbed the treasure first. Try again!")
        return

    elif first == "left":
        print(r'''
                   __/___            
             _____/______|           
     _______/_____\_______\_____     
     \              < < <       |    
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
        slow_print("Nice move! You took the left path and reached the harbor. 🌊\n")

        # --- Second Choice ---
        second = input("You see the sea ahead. Do you Swim across or Wait for a ship? ").strip().lower()
        if second == "swim":
            print(r'''
                   .-=-.  
             .--.-(`-.__.`)       
            ((    `-.__.-'   
             `--'`--'      
             ><(((º>     ><(((º> 
        ''')
            slow_print("😨 A Great White Shark attacked you mid-swim. Game over!")
            return

        elif second == "wait":
            print(r'''
                        |    |    |
                       )_)  )_)  )_)
                      )___))___))___)\
                   ____|____|____|____\__
          ---------\                   /---------
            ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
                     ^^^^      ^^^^
                          ^^^
            ''')
            slow_print("Smart! You waited and boarded a pirate ship safely! ⛵")
            slow_print("After days of sailing, you reach Treasure Island... 🏝️\n")

            print(r'''
  _______                          _     _             _ 
 |__   __|                        (_)   | |           | |
    | |_ __ ___  ___ __ _ _ __ ___ _ ___| | __ _ _ __ | |
    | | '__/ _ \/ __/ _` | '__/ _ \ / __| |/ _` | '_ \| |
    | | | |  __/ (_| (_| | | |  __/ \__ \ | (_| | | | | |
    |_|_|  \___|\___\__, |_|  \___|_|___/_|\__,_|_| |_|_|
                     __/ |                                
                    |___/                                 
            ''')
            # --- Third Choice ---
            third = input("You can either Dig or Explore the Cave. What do you choose? ").strip().lower()
            if third == "dig":
                print(r'''
                      _.--.
                  _.-'_:-'||
              _.-'_.-::::'||
         _.-:'_.-::::::'  ||
       .'`-.-:::::::'     ||
      /.'`;|:::::::'      ||_
     ||   ||::::::'     _.;._'-._
     ||   ||:::::'  _.-!oo @.!-._'-.
     \'.  ||:::::.-!()oo @!()@.-'_.|
      '.'-;|:.-'.&$@.& ()$%-'o.'\U||
        `>'-.!@%()@'@_%-'_.-o _.|'||
         ||-._'-.@.-'_.-' _.-o  |'||
         ||=[ '-._.-\U/.-'    o |'||
         || '-.]=|| |'|      o  |'||
         ||      || |'|        _| ';
         ||      || |'|    _.-'_.-'
         |'-._   || |'|_.-'_.-'
          '-._'-.|| |' `_.-'
              '-.||_/.-'
                ''')
                slow_print("💰 You found the legendary treasure! You win!")
            elif third == "cave":
                print(r'''
                ___   .--.
          .--.-"   "-' .- |
         / .-,`          .'  
         \   `           \  
          '.            ! \ 
            |     !  .--.  |
            \        '--'  /. __
             `.  `.       /.-'  `-
               `-.___.--'`
                ''')
                slow_print("😱 A giant bear was hibernating inside. You became its dinner. Game over.")
            else:
                slow_print("You hesitated too long... night fell and pirates took the gold. 💀")
        else:
            slow_print("You tripped on the dock and fell into the sea! Game over. 🌊")
    else:
        slow_print("You stood still... lost in thought. The adventure fades away. ☠️")

# --- Run the game ---
if __name__ == "__main__":
    treasure_island()