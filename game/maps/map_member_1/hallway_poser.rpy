# Persistent Variables for Hallway Objects (Trash Bin, Handkerchief)
default persistent.m1_hall_bin_x = 1400
default persistent.m1_hall_bin_y = 700
default persistent.m1_hall_bin_zoom = 0.5

default persistent.m1_hall_towel_x = 600
default persistent.m1_hall_towel_y = 780
default persistent.m1_hall_towel_zoom = 0.4

# Poser Logic
default m1_hall_poser_active = False
default m1_hall_poser_target = "bin" # "bin" or "towel"

init python:
    def m1_hall_get_pos(target):
        if target == "bin":
            return (persistent.m1_hall_bin_x, persistent.m1_hall_bin_y, persistent.m1_hall_bin_zoom)
        elif target == "towel":
            return (persistent.m1_hall_towel_x, persistent.m1_hall_towel_y, persistent.m1_hall_towel_zoom)
        return (0, 0, 1.0)
        
    def m1_hall_adjust(target, dx=0, dy=0, dz=0):
        if target == "bin":
            persistent.m1_hall_bin_x += dx
            persistent.m1_hall_bin_y += dy
            persistent.m1_hall_bin_zoom += dz
        elif target == "towel":
            persistent.m1_hall_towel_x += dx
            persistent.m1_hall_towel_y += dy
            persistent.m1_hall_towel_zoom += dz
            
    def m1_hall_print_code():
        print(f"default persistent.m1_hall_bin_x = {persistent.m1_hall_bin_x}")
        print(f"default persistent.m1_hall_bin_y = {persistent.m1_hall_bin_y}")
        print(f"default persistent.m1_hall_bin_zoom = {persistent.m1_hall_bin_zoom}")
        print(f"default persistent.m1_hall_towel_x = {persistent.m1_hall_towel_x}")
        print(f"default persistent.m1_hall_towel_y = {persistent.m1_hall_towel_y}")
        print(f"default persistent.m1_hall_towel_zoom = {persistent.m1_hall_towel_zoom}")
        renpy.notify("Code copied to console!")

screen m1_hallway_poser():
    zorder 300
    
    if m1_hall_poser_active:
        frame:
            xalign 1.0
            yalign 0.5
            padding (15, 15)
            background Solid("#000000DD")
            
            vbox:
                spacing 8
                text "HALLWAY POSER" size 14 color "#0f0" bold True
                
                # Target Selection
                hbox:
                    spacing 5
                    textbutton "Bin":
                        action SetVariable("m1_hall_poser_target", "bin")
                        text_color ("#0f0" if m1_hall_poser_target == "bin" else "#888")
                    textbutton "Towel":
                        action SetVariable("m1_hall_poser_target", "towel")
                        text_color ("#0f0" if m1_hall_poser_target == "towel" else "#888")
                
                # Coords
                $ pos = m1_hall_get_pos(m1_hall_poser_target)
                text f"X: {pos[0]} Y: {pos[1]} Z: {pos[2]:.2f}" size 12 color "#fff"
                
                # Controls
                hbox:
                    textbutton "◀":
                        action Function(m1_hall_adjust, m1_hall_poser_target, dx=-10)
                    textbutton "▲":
                        action Function(m1_hall_adjust, m1_hall_poser_target, dy=-10)
                    textbutton "▼":
                        action Function(m1_hall_adjust, m1_hall_poser_target, dy=10)
                    textbutton "▶":
                        action Function(m1_hall_adjust, m1_hall_poser_target, dx=10)
                
                hbox:
                    textbutton "Zoom -":
                        action Function(m1_hall_adjust, m1_hall_poser_target, dz=-0.05)
                    textbutton "Zoom +":
                        action Function(m1_hall_adjust, m1_hall_poser_target, dz=0.05)

                textbutton "Copy Code":
                    action Function(m1_hall_print_code)
                    text_color "#ff0"
                
                textbutton "Close":
                    action SetVariable("m1_hall_poser_active", False)
                    text_color "#f00"
    else:
        textbutton "HALL":
            xalign 0.98
            yalign 0.45
            action SetVariable("m1_hall_poser_active", True)
            text_size 14
            text_color "#0f0"
