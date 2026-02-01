# Poser Tool - Controls EXISTING characters on screen
# NO preview character - adjusts the actual displayed characters directly

default m1_poser_active = False
default m1_poser_target = "v"  # v, l, e, s, t
default m1_poser_mode = "sel"  # sel = Selection Screen, story = Story Scenes

init python:
    def m1_poser_get_x():
        t = store.m1_poser_target
        if store.m1_poser_mode == "sel":
            val = getattr(persistent, f"m1_sel_{t}_x", 500)
        else:
            val = getattr(persistent, f"m1_{t}_xpos", 500)
        return val if val is not None else 500
    
    def m1_poser_get_y():
        t = store.m1_poser_target
        if store.m1_poser_mode == "sel":
            val = getattr(persistent, f"m1_sel_{t}_y", 500)
        else:
            val = getattr(persistent, f"m1_{t}_ypos", 800)
        return val if val is not None else 800
    
    def m1_poser_get_z():
        t = store.m1_poser_target
        if store.m1_poser_mode == "sel":
            val = getattr(persistent, f"m1_sel_{t}_zoom", 1.0)
        else:
            val = getattr(persistent, f"m1_{t}_zoom", 1.0)
        return val if val is not None else 1.0

    def m1_poser_set_x(val):
        t = store.m1_poser_target
        if store.m1_poser_mode == "sel":
            setattr(persistent, f"m1_sel_{t}_x", int(val))
        else:
            setattr(persistent, f"m1_{t}_xpos", int(val))
        renpy.restart_interaction()
    
    def m1_poser_set_y(val):
        t = store.m1_poser_target
        if store.m1_poser_mode == "sel":
            setattr(persistent, f"m1_sel_{t}_y", int(val))
        else:
            setattr(persistent, f"m1_{t}_ypos", int(val))
        renpy.restart_interaction()
    
    def m1_poser_set_z(val):
        t = store.m1_poser_target
        if store.m1_poser_mode == "sel":
            setattr(persistent, f"m1_sel_{t}_zoom", val)
        else:
            setattr(persistent, f"m1_{t}_zoom", val)
        renpy.restart_interaction()

    def m1_poser_adjust_x(delta):
        m1_poser_set_x(m1_poser_get_x() + delta)
    
    def m1_poser_adjust_y(delta):
        m1_poser_set_y(m1_poser_get_y() + delta)
    
    def m1_poser_adjust_z(delta):
        m1_poser_set_z(max(0.1, m1_poser_get_z() + delta))

    def m1_poser_get_flip():
        t = store.m1_poser_target
        if store.m1_poser_mode == "sel":
            val = getattr(persistent, f"m1_sel_{t}_xzoom", None)
        else:
            val = getattr(persistent, f"m1_{t}_xzoom", None)
        return val if val is not None else 1.0
    
    def m1_poser_toggle_flip():
        t = store.m1_poser_target
        current = m1_poser_get_flip()
        new_val = -1.0 if current > 0 else 1.0
        if store.m1_poser_mode == "sel":
            setattr(persistent, f"m1_sel_{t}_xzoom", new_val)
        else:
            setattr(persistent, f"m1_{t}_xzoom", new_val)
        renpy.restart_interaction()

# DEV Button overlay
screen m1_dev_overlay():
    zorder 1000
    
    textbutton "DEV":
        xpos 10
        ypos 10
        text_size 28
        text_color "#0f0"
        text_outlines [(2, "#000", 0, 0)]
        action ToggleVariable("m1_poser_active")

# Poser Control Panel - NO PREVIEW CHARACTER
screen m1_poser_tool():
    zorder 999
    
    if m1_poser_active:
        # Control Panel Only - no character preview!
        frame:
            xalign 1.0
            yalign 0.0
            xmargin 10
            ymargin 50
            padding (15, 15)
            background Solid("#000000F0")
            
            vbox:
                spacing 8
                
                text "🎯 POSER" size 22 color "#0f0" bold True
                
                # Mode
                hbox:
                    spacing 10
                    textbutton "Selection":
                        action SetVariable("m1_poser_mode", "sel")
                        text_size 14
                        text_color ("#0f0" if m1_poser_mode == "sel" else "#888")
                    textbutton "Story":
                        action SetVariable("m1_poser_mode", "story")
                        text_size 14
                        text_color ("#0f0" if m1_poser_mode == "story" else "#888")
                
                null height 5
                
                # Character
                text "Char:" color "#aaa" size 12
                hbox:
                    spacing 6
                    for c in ["v", "l", "e", "s", "t", "c1", "c2"]:
                        textbutton c.upper():
                            action SetVariable("m1_poser_target", c)
                            text_size 16
                            text_color ("#0f0" if m1_poser_target == c else "#fff")
                
                null height 10
                
                # X
                $ cur_x = m1_poser_get_x()
                text f"X: {int(cur_x)}" color "#fff" size 14
                hbox:
                    spacing 3
                    textbutton "◀◀" action Function(m1_poser_adjust_x, -50) text_size 16
                    textbutton "◀" action Function(m1_poser_adjust_x, -10) text_size 16
                    textbutton "▶" action Function(m1_poser_adjust_x, 10) text_size 16
                    textbutton "▶▶" action Function(m1_poser_adjust_x, 50) text_size 16
                
                # Y
                $ cur_y = m1_poser_get_y()
                text f"Y: {int(cur_y)}" color "#fff" size 14
                hbox:
                    spacing 3
                    textbutton "▲▲" action Function(m1_poser_adjust_y, -50) text_size 16
                    textbutton "▲" action Function(m1_poser_adjust_y, -10) text_size 16
                    textbutton "▼" action Function(m1_poser_adjust_y, 10) text_size 16
                    textbutton "▼▼" action Function(m1_poser_adjust_y, 50) text_size 16

                # Zoom
                $ cur_z = m1_poser_get_z()
                text f"Zoom: {cur_z:.2f}" color "#fff" size 14
                hbox:
                    spacing 3
                    textbutton "−" action Function(m1_poser_adjust_z, -0.1) text_size 18
                    textbutton "+" action Function(m1_poser_adjust_z, 0.1) text_size 18
                
                # Flip
                $ is_flipped = m1_poser_get_flip() < 0
                textbutton ("🔄 Flip: ON" if is_flipped else "🔄 Flip: OFF"):
                    action Function(m1_poser_toggle_flip)
                    text_size 14
                    text_color ("#0f0" if is_flipped else "#fff")
                
                null height 10
                
                text "Changes save automatically!" size 10 color "#888"
                
                textbutton "✕ Close":
                    action SetVariable("m1_poser_active", False)
                    text_size 14
                    text_color "#f00"
