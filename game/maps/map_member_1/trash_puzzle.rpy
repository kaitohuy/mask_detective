# Trash Bin Puzzle - Drag & Drop mini-game
# Player must move trash items to find hidden lipstick

# Puzzle state
default m1_bin_open = False
default m1_bin_paper1_pos = (180, 140)
default m1_bin_paper2_pos = (230, 170)
default m1_bin_banana_pos = (200, 190)
default m1_bin_paper3_pos = (260, 155)
default m1_lipstick_found = False

init python:
    def m1_check_lipstick_clickable():
        """Check if trash items are moved enough to reveal lipstick for clicking"""
        # Lipstick is at position (210, 185)
        # Check if any trash is still covering it
        lipstick_x, lipstick_y = 210, 185
        lipstick_size = 40  # approximate size
        
        positions = [
            store.m1_bin_paper1_pos,
            store.m1_bin_paper2_pos, 
            store.m1_bin_paper3_pos,
            store.m1_bin_banana_pos
        ]
        
        # Check each trash item - if overlapping lipstick area, not clickable
        for pos_x, pos_y in positions:
            # Check if this trash overlaps with lipstick area
            if (abs(pos_x - lipstick_x) < 60 and abs(pos_y - lipstick_y) < 60):
                return False
        
        return True

screen m1_trash_bin_puzzle():
    tag menu
    modal True
    
    # Dark background
    add Solid("#000000E0")
    
    # Bin top view - centered and properly sized
    fixed:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 400
        
        # Bin background
        add "images/map01/object/bin_top_view.png":
            xalign 0.5
            yalign 0.5
            fit "contain"
        
        # === LIPSTICK - Always visible at BOTTOM layer ===
        # But only clickable when trash is moved away
        if not m1_lipstick_found:
            if m1_check_lipstick_clickable():
                imagebutton:
                    idle Transform("images/map01/object/lipstick.png", zoom=0.2)
                    hover Transform("images/map01/object/lipstick.png", zoom=0.22, matrixcolor=TintMatrix("#ffff88"))
                    xpos 210
                    ypos 185
                    action Return("found_lipstick")
            else:
                # Show lipstick but not clickable (covered by trash)
                add Transform("images/map01/object/lipstick.png", zoom=0.2):
                    xpos 210
                    ypos 185
        
        # === TRASH ITEMS - On TOP, covering lipstick ===
        
        # Paper 1
        drag:
            drag_name "paper1"
            xpos m1_bin_paper1_pos[0]
            ypos m1_bin_paper1_pos[1]
            draggable True
            droppable False
            dragged m1_on_paper1_dragged
            
            add "images/map01/object/paper_bin.png":
                zoom 0.18
        
        # Paper 2 (directly on lipstick)
        drag:
            drag_name "paper2"
            xpos m1_bin_paper2_pos[0]
            ypos m1_bin_paper2_pos[1]
            draggable True
            droppable False
            dragged m1_on_paper2_dragged
            
            add "images/map01/object/paper_bin.png":
                zoom 0.16
        
        # Paper 3
        drag:
            drag_name "paper3"
            xpos m1_bin_paper3_pos[0]
            ypos m1_bin_paper3_pos[1]
            draggable True
            droppable False
            dragged m1_on_paper3_dragged
            
            add "images/map01/object/paper_bin.png":
                zoom 0.14
        
        # Banana (on top)
        drag:
            drag_name "banana"
            xpos m1_bin_banana_pos[0]
            ypos m1_bin_banana_pos[1]
            draggable True
            droppable False
            dragged m1_on_banana_dragged
            
            add "images/map01/object/banana_bin.png":
                zoom 0.18
    
    # Instructions
    frame:
        xalign 0.5
        yalign 0.12
        padding (20, 10)
        background Solid("#000000CC")
        
        if m1_check_lipstick_clickable() and not m1_lipstick_found:
            text "💄 Click vào thỏi son!" size 20 color "#0f0"
        else:
            text "🗑 Kéo rác để tìm bằng chứng" size 18 color "#fff"
    
    # Close button
    textbutton "✕ Đóng":
        xalign 0.95
        yalign 0.05
        action Return("close")
        text_size 24
        text_color "#f00"
    
    # Fear warning
    if m1_has_fear("Mysophobia"):
        frame:
            xalign 0.5
            yalign 0.88
            padding (20, 10)
            background Solid("#ff0000AA")
            text "⚠ Sợ bẩn! -10 Mind" size 16 color "#fff"

init python:
    def m1_on_paper1_dragged(drags, drop):
        if drags:
            d = drags[0]
            store.m1_bin_paper1_pos = (int(d.x), int(d.y))
            renpy.restart_interaction()
        return None
    
    def m1_on_paper2_dragged(drags, drop):
        if drags:
            d = drags[0]
            store.m1_bin_paper2_pos = (int(d.x), int(d.y))
            renpy.restart_interaction()
        return None
    
    def m1_on_paper3_dragged(drags, drop):
        if drags:
            d = drags[0]
            store.m1_bin_paper3_pos = (int(d.x), int(d.y))
            renpy.restart_interaction()
        return None
    
    def m1_on_banana_dragged(drags, drop):
        if drags:
            d = drags[0]
            store.m1_bin_banana_pos = (int(d.x), int(d.y))
            renpy.restart_interaction()
        return None
