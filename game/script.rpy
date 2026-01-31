# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    scene bg room

    show eileen happy

    e "Chào mừng đến với dự án."
    e "Chọn map để bắt đầu phát triển/kiểm thử:"

    menu:
        "Map Member 1":
            jump map1_start
        
        "Map Member 2":
            jump map2_start
            
    # return statement is not strictly needed here as jumps will take over, 
    # but good to have if we fall through
    return

