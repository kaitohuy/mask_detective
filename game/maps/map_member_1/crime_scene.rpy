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
    
    # === POSER TOOL ===
    use m1_crime_scene_poser
    
    # Victor's dead body - using persistent positions
    if not m1_examined_body:
        imagebutton:
            idle Transform("images/map01/character/Victor_dead.png", zoom=persistent.m1_cs_body_zoom)
            hover Transform("images/map01/character/Victor_dead.png", zoom=persistent.m1_cs_body_zoom, matrixcolor=TintMatrix("#ffff88"))
            focus_mask True
            xpos persistent.m1_cs_body_x
            ypos persistent.m1_cs_body_y
            action Function(m1_examine_body)
            tooltip "Kham xac Victor"
    else:
        add "images/map01/character/Victor_dead.png":
            xpos persistent.m1_cs_body_x
            ypos persistent.m1_cs_body_y
            zoom persistent.m1_cs_body_zoom
    
    # Glass - using persistent positions
    if not m1_crime_collected_glass:
        imagebutton:
            idle Transform("images/map01/object/wine_glass.png", zoom=persistent.m1_cs_glass_zoom)
            hover Transform("images/map01/object/wine_glass.png", zoom=persistent.m1_cs_glass_zoom + 0.05, matrixcolor=TintMatrix("#ffff88"))
            focus_mask True
            xpos persistent.m1_cs_glass_x
            ypos persistent.m1_cs_glass_y
            action Function(m1_collect_item, "Ly ruou vo co vet son", "m1_crime_collected_glass")
            tooltip "Ly ruou vo"
    

    
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
                text "Hãy khám xác trước khi tiếp tục" size 18 color "#ff8"
            if m1_examined_body:
                textbutton "Tiếp tục":
                    action [Hide("m1_crime_scene"), Return("continue")]
                    text_size 20
                    text_color "#0f0"
            else:
                textbutton "Tiếp tục":
                    action NullAction()
                    text_size 20
                    text_color "#666"

# Inventory Screen - Clean design
init python:
    def m1_get_item_image(item_name):
        if "Ly ruou" in item_name or "Ly Rượu" in item_name: # Handle both cases
            return "images/map01/object/wine_glass.png"
        elif "Khan tay" in item_name or "Khăn Tay" in item_name:
            return "images/map01/object/handkerchief.png"
        return "images/map01/UI/bag.png" # Default icon

screen m1_inventory_screen():
    modal True
    zorder 200
    
    # Click outside to close
    button:
        xfill True
        yfill True
        background Solid("#00000099")
        action Hide("m1_inventory_screen")
    
    # Inventory panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 420
        ypadding 20
        xpadding 25
        background Solid("#1a1a1aF0")
        
        vbox:
            spacing 15
            
            # Header  
            hbox:
                xfill True
                spacing 12
                
                add "images/map01/UI/bag.png":
                    zoom 0.35
                    yalign 0.5
                
                text "TUI DO" size 22 color "#0f0" bold True yalign 0.5
                
                # Close button - right aligned
                hbox:
                    xalign 1.0
                    textbutton "X":
                        action Hide("m1_inventory_screen")
                        text_size 18
                        text_color "#f66"
                        text_hover_color "#f00"
            
            # Line separator
            add Solid("#444", xysize=(370, 1))
            
            # Items list
            vbox:
                spacing 6
                xsize 370
                
                if m1_inventory and len(m1_inventory) > 0:
                    for item in m1_inventory:
                        frame:
                            xfill True
                            padding (10, 8)
                            background Solid("#2a2a2a")
                            
                            hbox:
                                spacing 15
                                add m1_get_item_image(item):
                                    zoom 0.4
                                    maxsize (40, 40)
                                    yalign 0.5
                                    
                                text item size 15 color "#ddd" yalign 0.5
                else:
                    null height 30
                    text "( Trong )" size 16 color "#555" xalign 0.5 italic True
                    null height 30

