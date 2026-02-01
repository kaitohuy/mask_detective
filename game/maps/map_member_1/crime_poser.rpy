# Crime Scene Poser Tool
# Adjust positions of body, glass, handkerchief in crime scene

# Persistent positions for crime scene objects
default persistent.m1_cs_body_x = 960
default persistent.m1_cs_body_y = 750
default persistent.m1_cs_body_zoom = 0.8

default persistent.m1_cs_glass_x = 200
default persistent.m1_cs_glass_y = 700
default persistent.m1_cs_glass_zoom = 0.35

default persistent.m1_cs_towel_x = 1400
default persistent.m1_cs_towel_y = 720
default persistent.m1_cs_towel_zoom = 0.3

# Current target being edited
default m1_cs_poser_target = "body"  # body, glass, towel
default m1_cs_poser_active = False

init python:
    def m1_cs_get_pos(target):
        return (
            getattr(persistent, f"m1_cs_{target}_x", 500),
            getattr(persistent, f"m1_cs_{target}_y", 500),
            getattr(persistent, f"m1_cs_{target}_zoom", 1.0)
        )
    
    def m1_cs_adjust(target, dx=0, dy=0, dz=0):
        x = getattr(persistent, f"m1_cs_{target}_x", 500)
        y = getattr(persistent, f"m1_cs_{target}_y", 500)
        z = getattr(persistent, f"m1_cs_{target}_zoom", 1.0)
        setattr(persistent, f"m1_cs_{target}_x", x + dx)
        setattr(persistent, f"m1_cs_{target}_y", y + dy)
        setattr(persistent, f"m1_cs_{target}_zoom", max(0.1, z + dz))
        renpy.restart_interaction()
    
    def m1_cs_print_code():
        """Print code for current positions"""
        body = m1_cs_get_pos("body")
        glass = m1_cs_get_pos("glass")
        towel = m1_cs_get_pos("towel")
        
        code = f"""
# === CRIME SCENE POSITIONS ===
# Body: xpos {body[0]}, ypos {body[1]}, zoom {body[2]:.2f}
# Glass: xpos {glass[0]}, ypos {glass[1]}, zoom {glass[2]:.2f}
# Towel: xpos {towel[0]}, ypos {towel[1]}, zoom {towel[2]:.2f}
"""
        print(code)
        renpy.notify("Positions printed to console!")

screen m1_crime_scene_poser():
    zorder 300
    
    if m1_cs_poser_active:
        # Control Panel
        frame:
            xalign 1.0
            yalign 0.5
            padding (15, 15)
            background Solid("#000000DD")
            
            vbox:
                spacing 10
                
                text "🎬 CRIME SCENE POSER" size 16 color "#0f0" bold True
                
                null height 5
                
                # Target Selection
                text "Target:" size 12 color "#aaa"
                hbox:
                    spacing 5
                    textbutton "Xác":
                        action SetVariable("m1_cs_poser_target", "body")
                        text_size 12
                        text_color ("#0f0" if m1_cs_poser_target == "body" else "#888")
                    textbutton "Cốc":
                        action SetVariable("m1_cs_poser_target", "glass")
                        text_size 12
                        text_color ("#0f0" if m1_cs_poser_target == "glass" else "#888")
                    textbutton "Khăn":
                        action SetVariable("m1_cs_poser_target", "towel")
                        text_size 12
                        text_color ("#0f0" if m1_cs_poser_target == "towel" else "#888")
                
                null height 5
                
                # Position Display
                $ pos = m1_cs_get_pos(m1_cs_poser_target)
                text f"X: {pos[0]}" size 11 color "#fff"
                text f"Y: {pos[1]}" size 11 color "#fff"
                text f"Zoom: {pos[2]:.2f}" size 11 color "#fff"
                
                null height 5
                
                # Movement Controls
                text "Di chuyển:" size 12 color "#aaa"
                hbox:
                    spacing 3
                    textbutton "◀":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dx=-10)
                        text_size 14
                    textbutton "▲":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dy=-10)
                        text_size 14
                    textbutton "▼":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dy=10)
                        text_size 14
                    textbutton "▶":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dx=10)
                        text_size 14
                
                # Fast Movement
                hbox:
                    spacing 3
                    textbutton "◀◀":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dx=-50)
                        text_size 12
                    textbutton "▲▲":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dy=-50)
                        text_size 12
                    textbutton "▼▼":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dy=50)
                        text_size 12
                    textbutton "▶▶":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dx=50)
                        text_size 12
                
                null height 5
                
                # Zoom Controls
                text "Zoom:" size 12 color "#aaa"
                hbox:
                    spacing 5
                    textbutton "-":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dz=-0.05)
                        text_size 14
                    textbutton "+":
                        action Function(m1_cs_adjust, m1_cs_poser_target, dz=0.05)
                        text_size 14
                
                null height 10
                
                # Print Code
                textbutton "📋 Copy Code":
                    action Function(m1_cs_print_code)
                    text_size 12
                    text_color "#ff0"
                
                # Close
                textbutton "✕ Đóng":
                    action SetVariable("m1_cs_poser_active", False)
                    text_size 14
                    text_color "#f00"
    else:
        # Toggle Button (small)
        textbutton "🎬":
            xalign 0.98
            yalign 0.3
            action SetVariable("m1_cs_poser_active", True)
            text_size 24
