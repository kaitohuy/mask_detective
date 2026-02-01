
# --------------------------------------------------------------------------------
# INVENTORY & NOTEBOOK SYSTEM (MAP 02)
# --------------------------------------------------------------------------------

# --- VARIABLES ---
default m2_inventory = set()
default m2_notebook_list = []      # Danh sách ghi chú tự động
default m2_user_note = ""          # Ghi chú người chơi nhập

init python:
    def m2_add_note(content):
        # Thêm ghi chú nếu chưa tồn tại
        if content not in store.m2_notebook_list:
            store.m2_notebook_list.append(content)
            renpy.notify("Đã thêm vào sổ tay")

# --- SCREENS ---

# Nút mở Túi đồ & Sổ tay (Luôn hiện)
screen m2_hud():
    zorder 100
    
    # 1. Túi đồ (Góc trên phải)
    imagebutton:
        idle Transform("images/ui/bag.png", zoom=0.25)
        hover Transform("images/ui/bag.png", zoom=0.27)
        align (0.98, 0.05) 
        action Show("m2_inventory_popup")
        
    # 2. Sổ tay (Cạnh túi đồ)
    imagebutton:
        idle Transform("images/ui/closebook.png", zoom=0.25) 
        hover Transform("images/ui/closebook.png", zoom=0.27)
        align (0.93, 0.05)
        action Show("m2_notebook_popup")
        
    # 3. Nút KẾT TỘI (Cạnh sổ tay)
    textbutton "KẾT TỘI":
        text_font "fonts/kvn-97.ttf"
        text_size 25
        text_color "#fff"
        background Frame(Solid("#c0392b"), 10, 10) # Màu đỏ cảnh báo
        hover_background Frame(Solid("#e74c3c"), 10, 10)
        padding (10, 5)
        align (0.82, 0.05) # Dời sang trái để không đè lên sổ tay
        action Jump("m2_start_accusation")

# POPUP TÚI ĐỒ
screen m2_inventory_popup():
    zorder 101
    modal True
    
    button:
        background Solid("#000c")
        xfill True yfill True
        action Hide("m2_inventory_popup") 
        
    frame:
        background Frame("images/ui/ui_text.png", 50, 50)
        align (0.5, 0.5)
        padding (50, 50)
        xsize 800 ysize 600
        
        vbox:
            spacing 20
            text "TÚI ĐỒ CHỨNG CỨ" size 40 color "#f39c12" xalign 0.5 font "fonts/kvn-97.ttf"
            
            hbox:
                spacing 30
                box_wrap True
                
                # Objects
                if "note" in m2_inventory:
                    imagebutton:
                        idle Transform("images/map02/object/note_metting.png", zoom=0.15)
                        hover Transform("images/map02/object/note_metting.png", zoom=0.17)
                        action Show("m2_item_detail", item_image="images/map02/object/note_metting.png", item_desc="Giấy hẹn tìm thấy trong sách: 'Gặp tôi ở ban công tầng 2 lúc 1h sáng. Tôi sẽ giúp cậu xóa nợ.'")
                        tooltip "Mảnh giấy hẹn"

                if "teacup" in m2_inventory:
                    imagebutton:
                        idle Transform("images/map02/object/cup_tea.png", zoom=0.15)
                        hover Transform("images/map02/object/cup_tea.png", zoom=0.17)
                        action Show("m2_item_detail", item_image="images/map02/object/cup_tea.png", item_desc="Tách trà hoa cúc có cặn trắng. Bà Rosalind bị đánh thuốc mê.")
                        tooltip "Tách trà"
                
                if "pen" in m2_inventory:
                    imagebutton:
                        idle Transform("images/map02/object/broken_pen.png", zoom=0.15)
                        hover Transform("images/map02/object/broken_pen.png", zoom=0.17)
                        action Show("m2_item_detail", item_image="images/map02/object/broken_pen.png", item_desc="Cây bút Parker bị tòe đầu, dính máu khô.")
                        tooltip "Bút Parker hỏng"

                if "fishing_line" in m2_inventory:
                    imagebutton:
                        idle Transform("images/map02/object/fishing_line.png", zoom=0.15)
                        hover Transform("images/map02/object/fishing_line.png", zoom=0.17)
                        action Show("m2_item_detail", item_image="images/map02/object/fishing_line.png", item_desc="Cuộn dây cước dính máu ở giữa cuộn. Ai đó đã cầm vào đây để thực hiện thủ thuật 'Con dao mặt nạ'.")
                        tooltip "Cuộn dây cước"

    textbutton "ĐÓNG":
        align (0.9, 0.1)
        text_size 30
        action Hide("m2_inventory_popup")

default m2_draft_note = ""

init python:
    def m2_commit_note():
        if store.m2_draft_note.strip():
            # Thêm ghi chú người dùng vào danh sách chung, có đánh dấu
            store.m2_notebook_list.append("{color=#f1c40f}[Tôi]:{/color} " + store.m2_draft_note)
            store.m2_draft_note = ""
            renpy.restart_interaction()

# POPUP SỔ TAY (Giao diện mới: Input ở trên, List ở dưới)
screen m2_notebook_popup():
    zorder 101
    modal True
    
    button:
        background Solid("#000c")
        xfill True yfill True
        action Hide("m2_notebook_popup")
        
# POPUP SỔ TAY (Giao diện mới: Input ở trên, List ở dưới)
screen m2_notebook_popup():
    zorder 101
    modal True
    
    # Nền mờ tối
    button:
        background Solid("#000a")
        xfill True yfill True
        action Hide("m2_notebook_popup")
        
    frame:
        background Frame("images/ui/ui_text.png", 50, 50) 
        align (0.5, 0.5)
        padding (60, 50)
        xsize 900 ysize 650 # Tăng nhẹ kích thước
        
        vbox:
            spacing 25
            
            # --- 1. HEADER & INPUT ---
            # Tiêu đề nhỏ
            text "NHẬT KÝ ĐIỀU TRA" font "fonts/kvn-97.ttf" size 30 color "#3E2723" xalign 0.5 outlines [(1, "#fff", 1, 1)]
            
            hbox:
                spacing 15
                xfill True
                
                # Input Field được cách điệu
                frame:
                    background Frame(Solid("#5D4037"), 0, 0) # Viền mỏng hoặc nền tối nhẹ
                    ysize 60
                    xfill True
                    padding (15, 10)
                    # Input text màu đậm
                    input value VariableInputValue("m2_draft_note") length 100 color "#fff" size 24 pixel_width 650 prefix "{b}Ghi thêm:{/b} " font "fonts/kvn-97.ttf"
                
                # Nút LƯU (Style cái dấu mộc)
                textbutton "LƯU":
                    text_font "fonts/kvn-97.ttf"
                    text_size 24
                    text_color "#fff"
                    background Frame(Solid("#8D6E63"), 10, 10) # Màu nâu đất
                    hover_background Frame(Solid("#6D4C41"), 10, 10)
                    xsize 100 ysize 60
                    text_align (0.5, 0.5)
                    action Function(m2_commit_note)
            
            # Phím tắt Enter
            key "K_RETURN" action Function(m2_commit_note)
            key "K_KP_ENTER" action Function(m2_commit_note)

            # --- 2. DANH SÁCH GHI CHÚ ---
            
            # Đường kẻ ngang phân cách
            add Solid("#3E2723") xsize 780 ysize 2 xalign 0.5 alpha 0.5
            
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                yinitial 1.0 
                ysize 400
                
                vbox:
                    spacing 15
                    xfill True
                    
                    for i, note in enumerate(m2_notebook_list):
                        hbox:
                            spacing 10
                            # Bullet point hình tròn nhỏ
                            text "•" color "#5D4037" size 24 font "fonts/kvn-97.ttf" yalign 0.0
                            
                            # Nội dung Note
                            text "[note]" color "#3E2723" size 22 layout "subtitle" font "fonts/kvn-97.ttf" line_spacing 5
                        
                        # Đường kẻ mờ giữa các dòng (như giấy vở)
                        if i < len(m2_notebook_list) - 1:
                            add Solid("#3E2723") xsize 750 ysize 1 xalign 0.5 alpha 0.2

    # Nút ĐÓNG (Góc trên phải của frame thay vì góc màn hình)
    imagebutton:
        idle Transform("images/ui/closebook.png", zoom=0.20)
        hover Transform("images/ui/closebook.png", zoom=0.22)
        align (0.83, 0.18) # Căn chỉnh thủ công vào góc frame
        action Hide("m2_notebook_popup")

# Screen chi tiết
screen m2_item_detail(item_image, item_desc):
    modal True
    zorder 102
    
    button:
        background Solid("#000e")
        xfill True yfill True
        action Hide("m2_item_detail")
        
        vbox:
            align (0.5, 0.5)
            spacing 20
            
            add item_image zoom 1.0 align (0.5, 0.5) 
            
            frame:
                background Solid("#0008")
                padding (30, 30)
                text item_desc color "#fff" size 30 xalign 0.5 layout "subtitle" font "fonts/kvn-97.ttf"
