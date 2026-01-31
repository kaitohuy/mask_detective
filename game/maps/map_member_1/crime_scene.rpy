# Bathroom Crime Scene - Interactive Investigation Screen

# Track examination and collection states
default m1_examined_body = False
default m1_crime_collected_glass = False
default m1_crime_collected_towel = False

init python:
    def m1_examine_body():
        """Examine Victor's body and add clue"""
        store.m1_examined_body = True
        # Auto-add note about no attack signs, likely poisoning
        m1_add_clue("Xác Victor: Không có dấu hiệu bị tấn công, mép có bọt trắng - Khả năng cao bị đầu độc")
        renpy.notify("📝 Đã ghi chú vào sổ")
        renpy.restart_interaction()

    def m1_collect_item(item_name, var_name):
        """Collect an item and add to inventory"""
        setattr(store, var_name, True)
        if item_name not in store.m1_inventory:
            store.m1_inventory.append(item_name)
        renpy.notify(f"+ {item_name}")
        renpy.restart_interaction()

# Crime Scene Screen - Victor's body with collectible evidence
screen m1_crime_scene():
    tag menu
    modal True
    
    # Background
    add "bg m1_bathroom"
    
    # Victor's dead body (center-bottom) - clickable to examine
    if not m1_examined_body:
        imagebutton:
            idle Transform("images/map01/character/Victor_dead.png", zoom=0.8)
            hover Transform("images/map01/character/Victor_dead.png", zoom=0.8, matrixcolor=TintMatrix("#ffff88"))
            xalign 0.5
            yalign 0.85
            action Function(m1_examine_body)
            tooltip "🔍 Khám xác Victor"
    else:
        # After examination, just show the body
        add "images/map01/character/Victor_dead.png":
            xalign 0.5
            yalign 0.85
            zoom 0.8
    
    # Glass - left side (REPLACE with actual image path if available)
    if not m1_crime_collected_glass:
        imagebutton:
            # Use placeholder or actual image
            idle Solid("#ff6b6b80", xysize=(100, 100))  # Red placeholder for glass
            hover Solid("#ff6b6b", xysize=(100, 100))
            xpos 300
            ypos 750
            action Function(m1_collect_item, "Ly rượu vỡ có vết son", "m1_crime_collected_glass")
            tooltip "🍷 Ly rượu vỡ"
    
    # Towel - right side (REPLACE with actual image path if available)
    if not m1_crime_collected_towel:
        imagebutton:
            # Use placeholder or actual image
            idle Solid("#4ecdc480", xysize=(120, 80))  # Green placeholder for towel
            hover Solid("#4ecdc4", xysize=(120, 80))
            xpos 1450
            ypos 780
            action Function(m1_collect_item, "Khăn tay có chữ E thêu", "m1_crime_collected_towel")
            tooltip "🧣 Khăn tay"
    
    # Tooltip display
    $ tooltip = GetTooltip()
    if tooltip:
        frame:
            xalign 0.5
            yalign 0.05
            padding (20, 10)
            background Solid("#000000CC")
            text "[tooltip]" size 28 color "#fff"
    
    # Status panel (top-left)
    frame:
        xalign 0.02
        yalign 0.02
        padding (15, 10)
        background Solid("#000000CC")
        
        vbox:
            spacing 5
            text "🔍 HIỆN TRƯỜNG" size 18 color "#0f0" bold True
            if m1_examined_body:
                text "✓ Đã khám xác" size 14 color "#8f8"
            else:
                text "• Click vào xác để khám" size 14 color "#ff8"
            text f"Vật phẩm: {len(m1_inventory)}" size 14 color "#fff"
    
    # Continue button (bottom)
    frame:
        xalign 0.5
        yalign 0.98
        padding (30, 15)
        background Solid("#000000AA")
        
        hbox:
            spacing 30
            if not m1_examined_body:
                text "⚠ Hãy khám xác trước khi tiếp tục" size 18 color "#ff8"
            if m1_examined_body:
                textbutton "✓ Tiếp tục":
                    action Return()
                    text_size 20
                    text_color "#0f0"
            else:
                textbutton "✓ Tiếp tục":
                    action NullAction()
                    text_size 20
                    text_color "#666"

# Inventory Screen - Enhanced design
screen m1_inventory_screen():
    tag menu
    modal True
    
    # Dim background
    add Solid("#00000080")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 450
        padding (25, 25)
        background Solid("#1a1a1aF5")
        
        vbox:
            spacing 12
            
            # Header
            hbox:
                xfill True
                hbox:
                    spacing 10
                    add "images/map01/UI/bag.png" zoom 0.4
                    text "TÚI ĐỒ" size 26 color "#0f0" bold True yalign 0.5
                textbutton "✕":
                    xalign 1.0
                    action Hide("m1_inventory_screen")
                    text_size 22
                    text_color "#f00"
            
            null height 5
            
            # Separator
            add Solid("#333", xysize=(450, 2))
            
            null height 5
            
            # Items list (scrollable viewport)
            viewport:
                scrollbars "vertical"
                mousewheel True
                xsize 450
                ysize 300
                
                vbox:
                    spacing 8
                    if m1_inventory:
                        for item in m1_inventory:
                            frame:
                                xfill True
                                padding (12, 8)
                                background Solid("#2a2a2a")
                                hbox:
                                    spacing 10
                                    text "📦" size 16
                                    text f"{item}" size 16 color "#fff"
                    else:
                        frame:
                            xfill True
                            ysize 100
                            background Solid("#222")
                            text "Túi rỗng" size 18 color "#666" xalign 0.5 yalign 0.5 italic True

