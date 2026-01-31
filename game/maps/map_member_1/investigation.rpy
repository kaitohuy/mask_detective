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
        add "bg m1_living_room"
        
        # Thomas (Left)
        imagebutton:
            idle Transform("images/map01/character/Thomas_Serve.png", zoom=0.55)
            hover Transform("images/map01/character/Thomas_Serve.png", zoom=0.58, matrixcolor=TintMatrix("#ffff88"))
            xpos 80
            ypos 420
            action Return("thomas")
            tooltip "Thomas - Người hầu"
        
        # Leonard (Left-Center)
        imagebutton:
            idle Transform("images/map01/character/leonard_stand.png", zoom=0.55)
            hover Transform("images/map01/character/leonard_stand.png", zoom=0.58, matrixcolor=TintMatrix("#ffff88"))
            xpos 400
            ypos 380
            action Return("leonard")
            tooltip "Leonard - Em trai Victor"
        
        # Sophia (Right-Center)
        imagebutton:
            idle Transform("images/map01/character/sophia_stand.png", zoom=0.55)
            hover Transform("images/map01/character/sophia_stand.png", zoom=0.58, matrixcolor=TintMatrix("#ffff88"))
            xpos 850
            ypos 400
            action Return("sophia")
            tooltip "Sophia - Vợ Victor"
        
        # Elena (Right)
        imagebutton:
            idle Transform("images/map01/character/elena_after_killed_stand.png", zoom=0.55)
            hover Transform("images/map01/character/elena_after_killed_stand.png", zoom=0.58, matrixcolor=TintMatrix("#ffff88"))
            xpos 1250
            ypos 380
            action Return("elena")
            tooltip "Elena - Cô của Sophia"
        
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
        add "bg m1_hallway"
        
        # Trash Bin - clickable to open puzzle
        imagebutton:
            idle Transform("images/map01/object/bin.png", zoom=0.5)
            hover Transform("images/map01/object/bin.png", zoom=0.55, matrixcolor=TintMatrix("#ffff88"))
            xpos 1400
            ypos 700
            action Return("open_trash")
            tooltip "🗑 Thùng rác"
        
        # Handkerchief on floor
        if "Khăn Tay" not in m1_inventory:
            imagebutton:
                idle Transform("images/map01/object/handkerchief.png", zoom=0.4)
                hover Transform("images/map01/object/handkerchief.png", zoom=0.45, matrixcolor=TintMatrix("#ffff88"))
                xpos 600
                ypos 780
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
        add "bg m1_bathroom"
        
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
        add "images/map01/BG/Main_hall.png"
        
        # Just a transition area now
        frame:
            xalign 0.5
            yalign 0.5
            padding (30, 20)
            background Solid("#00000080")
            text "Sảnh chính - Không có gì đáng chú ý ở đây." size 20 color "#aaa"
        
        # Up -> Living Room
        imagebutton:
            idle Transform("images/map01/UI/arrow4.png", zoom=0.8)
            hover Transform("images/map01/UI/arrow4.png", zoom=0.9, matrixcolor=TintMatrix("#ffff88"))
            xalign 0.5
            ypos 80
            action SetVariable("m1_current_area", "living_room")
    
    # === TOOLTIP ===
    $ tooltip = GetTooltip()
    if tooltip:
        frame:
            xalign 0.5
            yalign 0.05
            padding (20, 10)
            background Solid("#000000CC")
            text "[tooltip]" size 22 color "#fff"
    
    # === STATUS BAR (Bottom) ===
    frame:
        xalign 0.0
        yalign 1.0
        xsize 400
        padding (15, 12)
        background Solid("#000000CC")
        
        hbox:
            spacing 20
            text "🧠 [m1_mind]" size 16 color "#0f0"
            text "⏰ [m1_time]" size 16 color "#ff0"
            text "📍 [m1_current_area]" size 14 color "#aaa"
    
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
