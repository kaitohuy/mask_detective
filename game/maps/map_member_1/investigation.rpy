# Investigation Hub - Point-and-click with arrow navigation
# 4 Areas: Main Hall, Hallway, Bathroom, Living Room

# Current area tracker
default m1_current_area = "living_room"

# Track who has been interrogated
default m1_interrogated_thomas = False
default m1_interrogated_leonard = False  
default m1_interrogated_sophia = False
default m1_interrogated_elena = False

# Area data for arrow navigation
# living_room <-> hallway <-> bathroom
#      |
#  main_hall

screen m1_investigation_screen():
    tag menu
    modal True
    
    # === AREA: LIVING ROOM (Characters here) ===
    if m1_current_area == "living_room":
        add Transform("images/map01/BG/Living_room.png", size=(1920, 1080))
        
        # === POSER TOOL ===
        use m1_investigation_poser
        
        # Thomas (Left)
        imagebutton:
            idle Transform("images/map01/character/Thomas_Serve.png", zoom=persistent.m1_inv_thomas_zoom)
            hover Transform("images/map01/character/Thomas_Serve.png", zoom=persistent.m1_inv_thomas_zoom + 0.03, matrixcolor=TintMatrix("#ffff88"))
            focus_mask True
            xpos persistent.m1_inv_thomas_x
            ypos persistent.m1_inv_thomas_y
            action Return("thomas")
            tooltip "Thomas - Nguoi hau"
        
        # Leonard (Left-Center)
        imagebutton:
            idle Transform("images/map01/character/leonard_stand.png", zoom=persistent.m1_inv_leonard_zoom)
            hover Transform("images/map01/character/leonard_stand.png", zoom=persistent.m1_inv_leonard_zoom + 0.03, matrixcolor=TintMatrix("#ffff88"))
            focus_mask True
            xpos persistent.m1_inv_leonard_x
            ypos persistent.m1_inv_leonard_y
            action Return("leonard")
            tooltip "Leonard - Em trai Victor"
        
        # Sophia (Right-Center)
        imagebutton:
            idle Transform("images/map01/character/sophia_stand.png", zoom=persistent.m1_inv_sophia_zoom)
            hover Transform("images/map01/character/sophia_stand.png", zoom=persistent.m1_inv_sophia_zoom + 0.03, matrixcolor=TintMatrix("#ffff88"))
            focus_mask True
            xpos persistent.m1_inv_sophia_x
            ypos persistent.m1_inv_sophia_y
            action Return("sophia")
            tooltip "Sophia - Vo Victor"
        
        # Elena (Right)
        imagebutton:
            idle Transform("images/map01/character/elena_after_killed_stand.png", zoom=persistent.m1_inv_elena_zoom)
            hover Transform("images/map01/character/elena_after_killed_stand.png", zoom=persistent.m1_inv_elena_zoom + 0.03, matrixcolor=TintMatrix("#ffff88"))
            focus_mask True
            xpos persistent.m1_inv_elena_x
            ypos persistent.m1_inv_elena_y
            action Return("elena")
            tooltip "Elena - Co cua Sophia"
        
        # Navigation arrows
        # Right -> Hallway
        imagebutton:
            idle Transform("images/map01/UI/arrow1.png", zoom=0.6)
            hover Transform("images/map01/UI/arrow1.png", zoom=0.7)
            xpos 1850
            ypos 500
            action SetVariable("m1_current_area", "hallway")
        
        # Down -> Main Hall
        imagebutton:
            idle Transform("images/map01/UI/arrow3.png", zoom=0.6)
            hover Transform("images/map01/UI/arrow3.png", zoom=0.7)
            xpos 960
            ypos 980
            action SetVariable("m1_current_area", "main_hall")
    
    # === AREA: HALLWAY (with trash bin) ===
    elif m1_current_area == "hallway":
        add Transform("bg m1_hallway", size=(1920, 1080))
        use m1_hallway_poser
        
        # Trash Bin - clickable to open puzzle
        imagebutton:
            idle Transform("images/map01/object/bin.png", zoom=persistent.m1_hall_bin_zoom)
            hover Transform("images/map01/object/bin.png", zoom=persistent.m1_hall_bin_zoom + 0.05, matrixcolor=TintMatrix("#ffff88"))
            focus_mask True
            xpos persistent.m1_hall_bin_x
            ypos persistent.m1_hall_bin_y
            action Return("open_trash")
            tooltip "🗑 Thùng rác"
        
        # Handkerchief on floor
        if "Khăn Tay" not in m1_inventory:
            imagebutton:
                idle Transform("images/map01/object/handkerchief.png", zoom=persistent.m1_hall_towel_zoom)
                hover Transform("images/map01/object/handkerchief.png", zoom=persistent.m1_hall_towel_zoom + 0.05, matrixcolor=TintMatrix("#ffff88"))
                focus_mask True
                xpos persistent.m1_hall_towel_x
                ypos persistent.m1_hall_towel_y
                action Return("search_hallway")
                tooltip "Khăn tay trên sàn"
        
        # Left -> Living Room
        imagebutton:
            idle Transform("images/map01/UI/arrow2.png", zoom=0.6)
            hover Transform("images/map01/UI/arrow2.png", zoom=0.7)
            xpos 20
            ypos 500
            action SetVariable("m1_current_area", "living_room")
        
        # Right -> Bathroom
        imagebutton:
            idle Transform("images/map01/UI/arrow1.png", zoom=0.6)
            hover Transform("images/map01/UI/arrow1.png", zoom=0.7)
            xpos 1850
            ypos 500
            action SetVariable("m1_current_area", "bathroom")
    
    # === AREA: BATHROOM ===
    elif m1_current_area == "bathroom":
        add Transform("bg m1_bathroom", size=(1920, 1080))
        
        # Victor's body
        add "images/map01/character/Victor_dead.png":
            xalign 0.5
            yalign 0.85
            zoom 0.7
        
        # Wine glass with lipstick mark
        if "Ly Rượu Vết Son" not in m1_evidence:
            imagebutton:
                idle Transform("images/map01/object/wine_glass.png", zoom=0.35)
                hover Transform("images/map01/object/wine_glass.png", zoom=0.4, matrixcolor=TintMatrix("#ffff88"))
                xpos 300
                ypos 750
                action Return("search_bathroom")
                tooltip "Ly rượu"
        
        # Left -> Hallway
        imagebutton:
            idle Transform("images/map01/UI/arrow2.png", zoom=0.6)
            hover Transform("images/map01/UI/arrow2.png", zoom=0.7)
            xpos 20
            ypos 500
            action SetVariable("m1_current_area", "hallway")
    
    # === AREA: MAIN HALL ===
    elif m1_current_area == "main_hall":
        add Transform("images/map01/BG/Main_hall.png", size=(1920, 1080))
        
        # Up -> Living Room
        imagebutton:
            idle Transform("images/map01/UI/arrow4.png", zoom=0.8)
            hover Transform("images/map01/UI/arrow4.png", zoom=0.9, matrixcolor=TintMatrix("#ffff88"))
            xalign 0.5
            ypos 80
            action SetVariable("m1_current_area", "living_room")
        
        # Hidden Capsule (Requires Thomas Affection 100)
        if m1_affection.get("Thomas", 0) >= 100 and "Vỏ Thuốc" not in m1_evidence:
            imagebutton:
                idle Transform("images/map01/object/xyanua.png", zoom=0.1) 
                hover Transform("images/map01/object/xyanua.png", zoom=0.12, matrixcolor=TintMatrix("#ffff88"))
                xpos 1600
                ypos 900
                action Return("found_capsule")
                tooltip "Vật thể lạ"
    
    # === TOOLTIP ===
    $ tooltip = GetTooltip()
    if tooltip:
        frame:
            xalign 0.5
            yalign 0.05
            padding (20, 10)
            background Solid("#000000CC")
            text "[tooltip]" size 22 color "#fff"
    

    
    # === JUDGMENT BUTTON (Bottom Right) ===
    frame:
        xalign 1.0
        yalign 1.0
        padding (15, 12)
        background Solid("#330000CC")
        
        textbutton "⚖ KẾT LUẬN":
            action Return("judgment")
            text_size 18
            text_color "#f00"
