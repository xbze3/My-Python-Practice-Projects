import time

# Variable Declaration 

global exit
global help
global amps
global volts
global resistance
global command
global result
global num_1
global num_2
global creater

exit = "exit"
help = "help"
amps = "I"
volts = "V"
resistance = "R"
creater = "createrCode"

# Aski Ark

print(                                                                                                     )
print(                                                                                                 )
time.sleep(0.2)
print("                                                                                   ____          ____                                             ")
time.sleep(0.2)
print("                                                                                  |oooo|        |oooo|                 ")
time.sleep(0.2)
print("                                                                                  |oooo| .----. |oooo|                 ")
time.sleep(0.2)
print("                                                                                  |Oooo|/\_||_/\|oooO|                 ")
time.sleep(0.2)
print("                                                                                  `----' / __ \ `----'                      ")
time.sleep(0.2)
print("                                                                                  ,/ |#|/\/__\/\|#| \,                        ")
time.sleep(0.2)
print("                ****                                                             /  \|#|| |/\| ||#|/  \                        ")
time.sleep(0.2)
print("                ********                                                        / \_/|_|| |/\| ||_|\_/ \                             ")
time.sleep(0.2)
print("                 ***********                                                   |_\/    o\=----=/o    \/_|          ")
time.sleep(0.2)
print("                      ************                                             <_>      |=\__/=|      <_>                        ")
time.sleep(0.2)
print("                        *************                                          <_>      |------|      <_>                  ")
time.sleep(0.2)
print("                           ******************                                  | |   ___|======|___   | |                              ")
time.sleep(0.2)
print("                              ********* **********                             //\\\ / |O|======|O| \ //\\\                            ")
time.sleep(0.2)
print("                                            ******                             |  | | |O+------+O| | |  |                                          ")
time.sleep(0.2)
print("(++++++++++)    (++++++++++)     (++++++++)     ***      (+++)                 |\/| \_+/        \+_/ |\/|                                          ")
time.sleep(0.2)
print("(++++++++++)    (++++++++++)     (+++++++++)     (++)   (+++++)                \__/ _|||        |||_ \__/                                 ")
time.sleep(0.2)
print("(+++)                  (+++)     (+++)  (+++)    (++)  (+++++++)                    | ||        || |                                     ")
time.sleep(0.2)
print("(+++)                 (+++)      (+++)  (+++)    (++) (+++) (+++)                  [==|]        [|==]                   ")
time.sleep(0.2)
print("(+++++++)            (+++)       (+++)  (++)     (++)(+++)   (+++)                 [===]        [===]                               ")
time.sleep(0.2)
print("(+++++++)           (+++)        (++++++++)      (++(+++)     (+++)                 >_<          >_<                             ")
time.sleep(0.2)
print("(+++)              (+++)         (+++ +++)       (+(+++++++++++++++)               || ||        || ||                     ")
time.sleep(0.2)
print("(+++)             (+++)          (+++  +++)       (+++++++++++++++++)              || ||        || ||                                ")
time.sleep(0.2)
print("(+++)            (+++)           (+++   +++)      (+++)         (+++)              || ||        || ||      -- Askii Art by Jay Thaler                             ")
time.sleep(0.2)
print("(++++++++++)    (++++++++++)     (+++    +++)     (+++)         (+++)            __|\_/|__    __|\_/|__                               ")
time.sleep(0.2)
print("(++++++++++)    (++++++++++)     (++++    +++)    (+++)         (+++)           /___n_n___\  /___n_n___\                                      ")
print(                                                                                          )
print(                                                                                           )



# Calculations 


while True:

    command = input("Operation: ")

    if command == help:
        print("I - Amps\nV - Volts\nR - Resistance")

    elif command == exit:
        break

    elif command == creater:
        print("xb_ze3")

    elif command == amps:
        num_1 = input("Enter number of Volts: ")
        num_2 = input("Enter the Resistance: ")
        result = float(num_1) / float(num_2)
        print("The answer is " + str(result))

    elif command == volts:
        num_1 = input("Enter number of Amps: ")
        num_2 = input("Enter the Resistance: ")
        result = float(num_1) * float(num_2)
        print("The answer is " + str(result))

    elif command == resistance:
        num_1 = input("Enter number of Volts: ")
        num_2 = input("Enter the Amps: ")
        result = float(num_1) / float(num_2)
        print("The answer is " + str(result))
        
    
