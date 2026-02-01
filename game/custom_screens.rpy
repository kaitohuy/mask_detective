# --- ĐỊNH NGHĨA FONT & ASSETS ---
# 1. Font: Bạn chép file font .ttf/.otf vào game/fonts/ (tạo thư mục nếu chưa có)
define my_font = "fonts/kvn-97.ttf" 

screen map_selection():
    tag menu
    
    # Background
    add "background_game" 

    default tooltip = ""

    # --- TIÊU ĐỀ ---
    text "CHỌN MÀN CHƠI":
        align (0.5, 0.1) 
        size 40
        font my_font # Áp dụng font
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]

    # --- KHUNG GRID (CHỨA MAP) ---
    # Bây giờ bạn có thể chỉnh align hoặc pos tùy ý
    frame:
        background "ui_grid_bg" 
        xsize 1350 
        ysize 550  
        padding (50, 50)
        
        # Vị trí thủ công: (0.5, 0.45) là giữa màn hình, hơi lệch lên trên
        align (0.5, 0.3) 
        
        # Grid chứa các map
        grid 2 1:
            spacing 50
            align (0.6, 0.5) # Căn giữa nội dung trong khung
            
            # Slot Map 01
            vbox:
                imagebutton:
                    idle "map01_idle"
                    hover "map01_hover"
                    action Jump("map1_start")
                    
                    # Âm thanh (Chép file vào game/audio/)
                    hover_sound "audio/hover.mp3" 
                    activate_sound "audio/mouse-click.mp3"

                    hovered SetScreenVariable("tooltip", "Dạ tiệc của những chiếc mặt nạ!")
                    unhovered SetScreenVariable("tooltip", "")
                
                text "Map 01":
                    xalign 0.5
                    yoffset 20
                    font my_font # Áp dụng font
                    color "#f37602"

            # Slot Map 02
            vbox:
                spacing 10 # Khoảng cách giữa ảnh và chữ
                imagebutton:
                    idle "map02_idle"
                    hover "map02_hover"
                    action Jump("map2_start") # Đã mở khóa Map 02

                    # Âm thanh
                    hover_sound "audio/hover.mp3"
                    activate_sound "audio/mouse-click.mp3"

                    hovered SetScreenVariable("tooltip", "Huyết nguyệt và lời nguyên mặt nạ!")
                    unhovered SetScreenVariable("tooltip", "")
                
                text "Map 02":
                    xalign 0.5
                    yoffset 20
                    font my_font # Áp dụng font
                    color "#f37602"


    # --- KHUNG TOOLTIP (MÔ TẢ) ---
    frame:
        background "ui_tooltip_bg" 
        xsize 1000 
        ysize 200 
        padding(40, 40)
        
        # Vị trí thủ công: nằm dưới khung grid
        align (0.5, 0.8) 
        
        vbox:
            align (0.5, 0.55)
            text tooltip:
            
                xalign 0.5
                layout "subtitle"
                text_align 0.5
                font my_font # Áp dụng font
                color "#f37602" 

    # --- TEXT THÔNG BÁO ---
    text "...Các map tiếp theo đang được triển khai tiếp...":
        align (0.5, 0.95) # Nằm sát mép dưới
        size 30
        font my_font # Áp dụng font
        color "#f39c12" 
        outlines [(1, "#000000", 1, 1)] 
