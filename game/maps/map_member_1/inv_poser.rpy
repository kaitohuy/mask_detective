# Investigation Poser Tool
# Adjust positions of characters in Living Room during investigation

# Persistent positions for investigation characters
default persistent.m1_inv_thomas_x = 80
default persistent.m1_inv_thomas_y = 420
default persistent.m1_inv_thomas_zoom = 0.55

default persistent.m1_inv_leonard_x = 400
default persistent.m1_inv_leonard_y = 380
default persistent.m1_inv_leonard_zoom = 0.55

default persistent.m1_inv_sophia_x = 850
default persistent.m1_inv_sophia_y = 400
default persistent.m1_inv_sophia_zoom = 0.55

default persistent.m1_inv_elena_x = 1250
default persistent.m1_inv_elena_y = 380
default persistent.m1_inv_elena_zoom = 0.55

# Current target being edited
default m1_inv_poser_target = "thomas"  # thomas, leonard, sophia, elena
default m1_inv_poser_active = False

init python:
    def m1_inv_get_pos(target):
        return (
            getattr(persistent, f"m1_inv_{target}_x", 500),
            getattr(persistent, f"m1_inv_{target}_y", 500),
            getattr(persistent, f"m1_inv_{target}_zoom", 1.0)
        )
    
    def m1_inv_adjust(target, dx=0, dy=0, dz=0):
        x = getattr(persistent, f"m1_inv_{target}_x", 500)
        y = getattr(persistent, f"m1_inv_{target}_y", 500)
        z = getattr(persistent, f"m1_inv_{target}_zoom", 1.0)
        setattr(persistent, f"m1_inv_{target}_x", x + dx)
        setattr(persistent, f"m1_inv_{target}_y", y + dy)
        setattr(persistent, f"m1_inv_{target}_zoom", max(0.1, z + dz))
        renpy.restart_interaction()
    
    def m1_inv_print_code():
        """Print code for current positions"""
        t = m1_inv_get_pos("thomas")
        l = m1_inv_get_pos("leonard")
        s = m1_inv_get_pos("sophia")
        e = m1_inv_get_pos("elena")
        
        code = f"""
# === INVESTIGATION CHARACTER POSITIONS ===
# Thomas: xpos {t[0]}, ypos {t[1]}, zoom {t[2]:.2f}
# Leonard: xpos {l[0]}, ypos {l[1]}, zoom {l[2]:.2f}
# Sophia: xpos {s[0]}, ypos {s[1]}, zoom {s[2]:.2f}
# Elena: xpos {e[0]}, ypos {e[1]}, zoom {e[2]:.2f}
"""
        print(code)
        renpy.notify("Positions printed to console!")

screen m1_investigation_poser():
    zorder 300
    
    if m1_inv_poser_active:
        # Control Panel
        frame:
            xalign 1.0
            yalign 0.5
            padding (15, 15)
            background Solid("#000000DD")
            
            vbox:
                spacing 8
                
                text "INVESTIGATION POSER" size 14 color "#0f0" bold True
                
                null height 3
                
                # Target Selection
                text "Target:" size 11 color "#aaa"
                hbox:
                    spacing 3
                    textbutton "Tho":
                        action SetVariable("m1_inv_poser_target", "thomas")
                        text_size 10
                        text_color ("#0f0" if m1_inv_poser_target == "thomas" else "#888")
                    textbutton "Leo":
                        action SetVariable("m1_inv_poser_target", "leonard")
                        text_size 10
                        text_color ("#0f0" if m1_inv_poser_target == "leonard" else "#888")
                hbox:
                    spacing 3
                    textbutton "Sop":
                        action SetVariable("m1_inv_poser_target", "sophia")
                        text_size 10
                        text_color ("#0f0" if m1_inv_poser_target == "sophia" else "#888")
                    textbutton "Ele":
                        action SetVariable("m1_inv_poser_target", "elena")
                        text_size 10
                        text_color ("#0f0" if m1_inv_poser_target == "elena" else "#888")
                
                null height 3
                
                # Position Display
                $ pos = m1_inv_get_pos(m1_inv_poser_target)
                text f"X: {pos[0]}" size 10 color "#fff"
                text f"Y: {pos[1]}" size 10 color "#fff"
                text f"Z: {pos[2]:.2f}" size 10 color "#fff"
                
                null height 3
                
                # Movement Controls
                hbox:
                    spacing 3
                    textbutton "◀":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dx=-10)
                        text_size 12
                    textbutton "▲":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dy=-10)
                        text_size 12
                    textbutton "▼":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dy=10)
                        text_size 12
                    textbutton "▶":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dx=10)
                        text_size 12
                
                # Fast Movement
                hbox:
                    spacing 3
                    textbutton "◀◀":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dx=-50)
                        text_size 10
                    textbutton "▲▲":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dy=-50)
                        text_size 10
                    textbutton "▼▼":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dy=50)
                        text_size 10
                    textbutton "▶▶":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dx=50)
                        text_size 10
                
                null height 3
                
                # Zoom Controls
                hbox:
                    spacing 5
                    textbutton "-":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dz=-0.05)
                        text_size 14
                    textbutton "+":
                        action Function(m1_inv_adjust, m1_inv_poser_target, dz=0.05)
                        text_size 14
                
                null height 8
                
                # Print Code
                textbutton "Copy":
                    action Function(m1_inv_print_code)
                    text_size 11
                    text_color "#ff0"
                
                # Close
                textbutton "X":
                    action SetVariable("m1_inv_poser_active", False)
                    text_size 14
                    text_color "#f00"
    else:
        # Toggle Button (small)
        textbutton "INV":
            xalign 0.98
            yalign 0.4
            action SetVariable("m1_inv_poser_active", True)
            text_size 14
            text_color "#0f0"
