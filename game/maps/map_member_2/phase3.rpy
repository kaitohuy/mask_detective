
label m2_phase3:
    # --- GIAI ĐOẠN 3: KHOẢNG LẶNG ĐIỀU TRA (INTERMISSION) ---
    play music m2_bgm_investigation fadein 2.0 loop
    
    # CẢNH 6: SỰ VẮNG MẶT CỦA ARTHUR (Confrontation)
    show screen m2_hud # Hiển thị HUD (Túi đồ + Sổ tay)
    scene bg map02_livingroom with fade
    
    show liam normal at right
    show arthur nervous at left
    show sebastian normal at center
    
    m2_liam "Rõ ràng là cậu! Mật mã chỉ có cậu biết. Cậu túng tiền nên đã trộm mặt nạ, bị dì cậu phát hiện nên ra tay sát hại!"
    
    m2_arthur "Không! Cháu không làm! Bác sĩ, sao ông lại đổ điêu?"
    
    m2_liam "Đừng chối nữa. Tôi sẽ gọi cảnh sát ngay khi bão tan."
    
    m2_arthur "Các người... Các người hùa nhau ép tôi vào đường cùng!"
    
    hide arthur with moveoutleft
    "Arthur hoảng loạn bỏ chạy ra khỏi phòng khách."
    
    m2_sebastian "Cậu chủ! Khoan đã!"
    
    m2_liam "Để mặc nó. Nó không chạy thoát khỏi hòn đảo này đâu."
    
    m2_player "{i}(Mọi chuyện diễn ra quá nhanh. Mình cần tự kiểm tra manh mối xác thực.){/i}"
    
    "HỆ THỐNG: BẮT ĐẦU ĐIỀU TRA TỰ DO."
    
    # Jump vào vòng lặp điều hướng
    jump m2_nav_loop

# ... (Phần Navigation Loop giữ nguyên) ...

# 4. PHÒNG KHÁCH (Sebastian & Clara)
label m2_loc_livingroom:
    scene bg map02_livingroom
    call screen m2_scr_livingroom

label m2_talk_sebastian:
    show sebastian normal at left
    m2_sebastian "Cậu chủ Arthur tuy ham chơi nhưng rất nhát gan. Cậu ấy không dám cầm dao đâu."
    jump m2_loc_livingroom

label m2_talk_clara:
    show clara normal at right
    if not m2_clue_arthur_note:
        m2_clara "Thưa... Tôi có thấy một chuyện lạ."
        m2_clara "Hồi chiều, sau khi bị bà chủ mắng, tôi thấy cậu Arthur lén lút kẹp một mảnh giấy nhỏ vào cuốn sách trên bàn làm việc của cậu ấy."
        m2_clara "Có vẻ cậu ấy đang giấu giếm cuộc hẹn nào đó."
        m2_player "{i}(Mảnh giấy trong sách? Mình nên đến phòng Arthur kiểm tra.){/i}"
        
        $ m2_add_note("Clara: Arthur giấu một mảnh giấy trong sách tại phòng cậu ấy.")
    else:
        m2_clara "Cậu Arthur chắc chắn vô tội..."
    jump m2_loc_livingroom

label m2_loc_livingroom_menu:
    # Menu phụ để tiếp tục hỏi hoặc rời đi
    menu:
        "Tiếp tục hỏi chuyện":
            jump m2_loc_livingroom
        "Rời đi":
            jump m2_nav_loop


# --------------------------------------------------------------------------------
# NAVIGATION LOOP
# --------------------------------------------------------------------------------
label m2_nav_loop:
    # Kiểm tra điều kiện hoàn thành Phase 3
    if m2_clue_teacup and m2_clue_transom and m2_clue_masks_scratched and m2_clue_arthur_note:
        jump m2_phase3_complete

    # Hiện menu chọn phòng (Hoặc dùng Screen Map nếu có, ở đây dùng menu text/screen arrows)
    # Vì user muốn mũi tên chuyển phòng tương tác trực quan
    
    # Mặc định đang ở Hành lang.
    scene bg map02_hallway
    
    "Bạn đang ở Hành lang tầng 2. Bạn muốn đi đâu?"
    
    call screen m2_phase3_map_selection
    
    # Kết quả trả về từ screen sẽ jump đến các label con
    # Screen này sẽ được định nghĩa ở dưới hoặc file navigation.rpy
    
    jump m2_nav_loop

# --------------------------------------------------------------------------------
# SCREEN MŨI TÊN (Đã có trong phase3_initial, nhưng cập nhật lại list phòng)
# --------------------------------------------------------------------------------
screen m2_phase3_map_selection():
    # Điều hướng: Trái (Gallery), Phải (Phòng Arthur), Xuống (Phòng Khách), Lên (Phòng Rosalind - Hiện trường)
    # Cần chỉnh lại navigation.rpy hoặc dùng arrow tùy chỉnh
    
    # 1. Mũi tên TRÁI -> GALLERY (Victor)
    imagebutton:
        idle "images/ui/arrow4.png" hover "images/ui/arrow4.png" at arrow_hover
        align (0.05, 0.5) action Jump("m2_loc_gallery")
    text "Phòng Tranh" align (0.05, 0.55) size 20

    # 2. Mũi tên PHẢI -> PHÒNG ARTHUR
    imagebutton:
        idle "images/ui/arrow1.png" hover "images/ui/arrow1.png" at arrow_hover
        align (0.95, 0.5) action Jump("m2_loc_arthur_room")
    text "Phòng Arthur" align (0.95, 0.55) size 20

    # 3. Mũi tên XUỐNG -> PHÒNG KHÁCH (Sebastian)
    imagebutton:
        idle "images/ui/arrow3.png" hover "images/ui/arrow3.png" at arrow_hover
        align (0.5, 0.95) action Jump("m2_loc_livingroom")
    text "Phòng Khách" align (0.5, 0.98) size 20
    
    # 4. Mũi tên LÊN (hoặc giữa) -> PHÒNG ROSALIND (Liam + Isabella đang đứng ngoài?)
    # Thực tế Player đang đứng ở Hành lang (Base) -> Click vào cửa phòng Rosalind để vào
    textbutton "Vào Phòng Rosalind":
        align (0.5, 0.4) text_size 30 background "#0008" 
        action Jump("m2_loc_rosalind_room")
    
    # Hiển thị Isabella và Liam đang đứng ở hành lang (để dễ tương tác)
    # Isabella
    imagebutton:
        focus_mask True
        idle Transform("isabella normal", zoom=0.85)
        hover Transform("isabella normal", zoom=0.85, matrixcolor=BrightnessMatrix(0.1))
        align (0.3, 0.85)
        action Jump("m2_talk_isabella")

    # Liam
    imagebutton:
        focus_mask True
        idle Transform("liam normal", zoom=0.85)
        hover Transform("liam normal", zoom=0.85, matrixcolor=BrightnessMatrix(0.1))
        align (0.7, 0.85)
        action Jump("m2_talk_liam")


# --------------------------------------------------------------------------------
# CÁC PHÒNG (LOCATIONS)
# --------------------------------------------------------------------------------

# 1. HÀNH LANG (BASE) - Isabella & Liam
label m2_talk_isabella:
    show isabella normal at center
    m2_isabella "Tôi sợ quá... Bà ấy chết thảm quá."
    m2_isabella "Mà lạ lắm, tôi thấy trên ô thoáng cửa phòng bà ấy có mấy vết xước mới tinh. Như ai đó kéo vật gì qua vậy."
    
    $ m2_clue_transom = True
    $ m2_add_note("Isabella: Thấy vết xước lạ trên ô thoáng cửa phòng Rosalind.")
    
    jump m2_nav_loop

label m2_talk_liam:
    show liam normal at center
    m2_liam "Cậu mau tìm bằng chứng đi. Tôi chắc chắn Arthur là hung thủ."
    jump m2_nav_loop

# 2. PHÒNG BÀ ROSALIND (HIỆN TRƯỜNG VỤ ÁN)
label m2_loc_rosalind_room:
    scene bg map02_rosalind_bedroom_dead
    "Phòng bà Rosalind. Mùi máu tanh hòa lẫn mùi thuốc sát trùng."
    call screen m2_investigation_rosalind
    jump m2_nav_loop

# 3. PHÒNG ARTHUR
label m2_loc_arthur_room:
    scene bg map02_arthur_room
    
    # Nút Túi đồ (đã global, nhưng gọi lại cho chắc nếu cần, hoặc bỏ qua nếu đã show ở phase3 start)
    # show screen m2_inventory_button 
    
    call screen m2_scr_arthur_room



# 5. PHÒNG TRANH (GALLERY) - Victor
label m2_loc_gallery:
    scene bg map02_gallery_empty
    call screen m2_scr_gallery

label m2_talk_victor:
    show victor normal at center
    m2_victor "200 cái mặt nạ! Biến mất trong nháy mắt. Giá trị của chúng phải lên tới hàng triệu đô."
    m2_victor "Lũ trộm này làm ăn ẩu thật. Chúng để lại đống mặt nạ trầy xước lung tung ở hiện trường."
    
    $ m2_clue_masks_scratched = True
    $ m2_add_note("Victor: Các mặt nạ ở hiện trường bị trầy xước nhiều.")
    
    jump m2_loc_gallery

screen empty_screen():
    modal True
    # Screen rỗng để chặn click cho đến khi bấm nút


screen m2_investigation_rosalind():
    modal True
    
    # Nút Quay lại (nếu chán)
    textbutton "QUAY LẠI HÀNH LANG":
        align (0.5, 0.95)
        action Return()
        
    # 1. Tách trà (Nếu chưa nhặt)
    if not m2_clue_teacup:
        imagebutton:
            idle Transform("images/map02/object/cup_tea.png", zoom=0.125)
            hover Transform("images/map02/object/cup_tea.png", zoom=0.13)
            # Tọa độ giả định trên bàn (phải căn chỉnh sau nếu lệch)
            align (0.3, 0.6) 
            action [
                SetVariable("m2_clue_teacup", True), 
                AddToSet(m2_inventory, "teacup"),
                Notify("Đã nhặt: Tách trà hoa cúc")
            ]
            tooltip "Tách trà hoa cúc"
            
    # Hiển thị tooltip khi hover
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" align (0.5, 0.1) color "#fff" outlines [(2, "#000", 0, 0)]

# --------------------------------------------------------------------------------
# KẾT THÚC PHASE 3
# --------------------------------------------------------------------------------
label m2_phase3_complete:
    scene bg map02_hallway
    m2_player "Mình đã thu thập đủ thông tin."
    m2_player "1. Bà Rosalind bị đánh thuốc mê (Cặn trà)."
    m2_player "2. Hung thủ dùng dây kéo qua ô thoáng (Vết xước cửa + mặt nạ)."
    m2_player "3. Arthur không bỏ trốn, cậu ta có hẹn ở Ban công lúc 1h sáng (Mảnh giấy)."
    
    "Bỗng nhiên..."
    return

# --------------------------------------------------------------------------------
# SCREEN TƯƠNG TÁC PHÒNG (INTERACTION SCREENS)
# --------------------------------------------------------------------------------

screen m2_scr_livingroom():
    # Hiển thị Sebastian & Clara (Click to talk)
    imagebutton:
        focus_mask True # Chỉ click vào phần hình ảnh nhân vật (bỏ qua trong suốt)
        idle Transform("sebastian normal", zoom=1.0)
        hover Transform("sebastian normal", zoom=1.0, matrixcolor=BrightnessMatrix(0.1))
        align (0.3, 0.85)
        action Jump("m2_talk_sebastian")
        
    imagebutton:
        focus_mask True
        idle Transform("clara normal", zoom=1.0)
        hover Transform("clara normal", zoom=1.0, matrixcolor=BrightnessMatrix(0.1))
        align (0.7, 0.85)
        action Jump("m2_talk_clara")

    # Nút Quay lại
    imagebutton:
        idle "images/ui/arrow3.png" hover "images/ui/arrow3.png" at arrow_hover
        align (0.5, 0.95)
        action Jump("m2_nav_loop")

screen m2_scr_gallery():
    # Victor (Click to talk)
    imagebutton:
        focus_mask True
        idle Transform("victor normal", zoom=1.0)
        hover Transform("victor normal", zoom=1.0, matrixcolor=BrightnessMatrix(0.1))
        align (0.5, 0.85)
        action Jump("m2_talk_victor")

    # Nút Quay lại (Mũi tên xuống)
    imagebutton:
        idle "images/ui/arrow3.png" hover "images/ui/arrow3.png" at arrow_hover
        align (0.5, 0.95)
        action Jump("m2_nav_loop")

screen m2_scr_arthur_room():
    # 1. Vật chứng: Mảnh giấy (Nếu chưa nhặt)
    if not m2_clue_arthur_note:
        imagebutton:
            idle Transform("images/map02/object/note_metting.png", zoom=0.125, blur=3.0) # Zoom nhỏ 0.125, mờ 3.0
            hover Transform("images/map02/object/note_metting.png", zoom=0.13, blur=3.0) # Giữ nguyên độ mờ khi hover
            align (0.5, 0.65) 
            action [
                SetVariable("m2_clue_arthur_note", True), 
                AddToSet(m2_inventory, "note"),
                Notify("Đã nhặt: Mảnh giấy hẹn")
            ]
            tooltip "Mảnh giấy kẹp trong sách"
            
    # Nút Quay lại
    imagebutton:
        idle "images/ui/arrow3.png" hover "images/ui/arrow3.png" at arrow_hover
        align (0.5, 0.95)
        action Jump("m2_nav_loop")
