#Pokomon
#x =print((str"

message = "message" #global variable
#exist everywhere
#local vs global variables
#int

pokemon_level = 0 #global
pokemon_name = "squirtle"

day=0
#FUNCTIONS
#def drawsquirtle()



def train():
    global pokemon_name
    print("Your "+ pokemon_name + " has trained hard by doing 100 pushups he is level " + str(pokemon_level + 1))
def Gym_battle():
    global pokemon_name
        print("your " + pokemon_name + " won a gym battle he is level " + str(pokemon_level +2))
def display_info():
    global pokemon_name
    print(pokemon_name + " is level " + str(pokemon_level))
    if pokemon_level < 6:
        print("""⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜
⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🏿⬛⬛⬜⬛🟦🟦🟦⬛🟦🟦⬛
⬛🟫🟦🟦🟦🟦🟦🟦🟦🟦🏿🟫🏿⬛🟦🟦🟦⬛🟦🟦🟦⬛
⬛🟦🟦🟦🟦⬜⬛🟦🟦🟦🏽🟫🟫🏿⬛🟦🟦⬛🟦🟦⬛⬜
⬛🟦🟦🟦🟦⬛🟫🟦🟦🟦⬜🟫🟫🟫⬛🟦⬛⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦⬛🟫🟦🟦🟦⬛⬜⬜🟫🟫⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦⬛⬛🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟦⬛⬛⬛⬛🟦🟦🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟨🟨⬛🟦🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨⬛⬛⬛⬛🏽🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟦⬛🟫🟨🟨🟨🟫⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛🟫🟫🟦⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
    if pokemon_level > 5 and pokemon_level < 11:
        print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜
⬜⬜⬛⬜⬜⬛⬛⬛⬛⬜⬛⬜⬜⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛🟦🟦🟦🟦🟪🟪⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬛🟪🟦🟦🟦🟦🟦◼️⬜⬛⬜⬛⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜
⬜⬜⬛🟦🟦🟦🟦🟦🟦◼️⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜
⬜⬛🟦🟦🟦🟦🟦🟦⬛🟪⬛⬜⬜⬛🟨⬛⬜⬛⬜⬜⬛⬛⬜⬛⬜⬜
⬜⬛🟦🟦🟦🟦🟦⬛⬜🟦🟦⬛⬛🟫🟨🟫⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬛🟦🟦🟦⬛⬛⬜⬜🟦⬛⬜⬜🟫🟨⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬛🟦🟦🟦🟦🟫⬜🟦🟪⬛⬛⬜🟫🟨🟨⬛⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬛🟦⬛🟦🟪🟦🟦🟦⬛⬛🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬛⬜🟦⬛⬛⬛⬛⬛🟨⬛🟦🟦🟦⬜🟫🟨⬛⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬜⬛⬜🟨🟨⬛⬜🟦🟦⬛⬜🟫🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨⬛🟦⬜⬛⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟦⬛⬛🟨⬛⬛🟨⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟦🟦⬛⬛🟨🟨⬛🟦⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟪🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
    if pokemon_level > 10:
        print("""⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜🏽🏽⬛⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬜⬛⬜🟫🟫🟫🟫⬛⬛⬛🏽🏽⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟦⬛⬛🟫🟫🟫🟫🟫🟫⬛⬜⬛⬛🏽⬛⬜⬜⬜⬜
⬜⬜⬜⬛🟦🟦🟦⬛⬛🟫⬛⬛🟫⬜⬜⬛⬛🏽⬛⬜⬜⬜⬜
⬜⬜⬛🟦🟦🟦🟦🟦🟦⬛🟦⬛🟫⬜🏽🏽🏽⬛⬜⬜⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟫🟫🏽🏽⬛🟫⬛⬜⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦⬛🟦🟦⬛🏽🏽🏽⬛⬛🟫🟫⬛⬜⬜⬜⬜
⬛🟦🟦🟦🟦🟦⬛⬜🟦🟦🟦⬛⬛⬛⬛⬛🏽🟫🟫⬛⬛⬛⬛
⬛🟦🟦🟦🟦⬛⬛🟦🟦🟨🟦⬛⬛🟦🟦🟦⬛🏽🟫⬛🟦🟦⬛
⬛⬜🟦🟦🟦🟦🟦🟦🟨🟨⬛🏽⬛🟦🟦🟦⬛🏽🟫⬛🟦⬛⬜
⬜⬛🟨🟨🟦🟦🟨🟨🟨⬛🏽⬛🟦🟦🟦🟦⬛🏽🏽⬛⬛⬜⬜
⬜⬜⬛⬛⬜🟨🟨⬛⬛🟨⬛🟦🟦🟦🟦⬛🟦⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🟨🟨⬛⬜🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨⬛⬛🟦🟦⬛🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛🟨🟨⬛⬜⬛⬛⬛⬛🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨⬛🟨⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜🟦🟦⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜
""")

def evolution():
    global pokemon_name
    if pokemon_level <= 4:
        pokemon_name = "squirtle"
    if pokemon_level > 4 and pokemon_level <= 10:
        pokemon_name = "Wartortle"
    if pokemon_level >= 10:
        pokemon_name = "blastoise"
    return pokemon_level
#main
print("welcome to Pokemon Evolution")
while True:
    day = day + 1
    print("It is day " + str(day))
    print("Select an activity for the day")
    print("""    1. Train
    2. Gym battle
    3. Rest(display info)
    4. Quit""")
    activty = int(input("Activity: "))
    if activty == 1:
        train()
        #evolution()
        pokemon_level = pokemon_level + 1
    if activty == 2:
        Gym_battle()
        #evolution()
        pokemon_level = pokemon_level + 2
    if activty == 3:
        display_info()
        #evolution()
    if activty == 4:
        break
    evolution()
