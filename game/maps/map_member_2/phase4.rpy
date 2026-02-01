


label m2_phase4:
    # --- GIAI ĐOẠN 4: VỤ ÁN THỨ HAI (MURDER 2) ---
    
    # Âm thanh: Kinh dị/Sốc
    play music m2_bgm_murder2 fadein 0.5 loop
    
    # CẢNH 8: TIẾNG THÉT TRONG MƯA (01:00 AM)
    scene black
    "01:00 AM."
    
    # SFX: Tiếng sấm
    play sound sfx_thunder 
    "ĐÙNG ĐOÀNG!!!"
    
    # SFX: Tiếng hét đàn ông (Arthur)
    play sound "audio/man-scream.mp3"
    "Một tiếng thét thất thanh ngắn ngủi bị tiếng mưa lấn át."
    
    scene bg map02_hallway
    m2_player "Tiếng hét ở phía sân sau!"
    
    show victor normal at center
    m2_victor "Có người rơi xuống! Phía sân sau!"
    
    # CẢNH 9 & 10: HIỆN TRƯỜNG ARTHUR
    scene bg map02_backyard with fade
    "Mưa tầm tã."
    
    "Arthur nằm chết trên hàng rào sắt nhọn bao quanh dinh thự."
    
    show liam normal at right
    m2_liam "Là Arthur. Cậu ta rơi trúng hàng rào sắt. Chết rồi."
    
    show sebastian normal at left
    "Sebastian nhặt một tờ giấy ướt sũng dưới đất."
    m2_sebastian "Có thư tuyệt mệnh: 'Tôi không chịu nổi nữa. Những chiếc mặt nạ ám ảnh tôi.'..."
    
    m2_liam "Và đây là cuộn dây cước trong túi quần cậu ta. Nó dính máu."
    m2_liam "Có lẽ hắn dùng nó để làm trò phù thủy trong phòng kín. Vụ án kết thúc rồi. Hắn tự sát vì hối hận."
    
    # Soi tay Arthur & Dây cước
    m2_player "Tôi tiến lại gần thi thể Arthur để kiểm tra kỹ hơn."
    
    call screen m2_scr_phase4_investigation
    
    m2_player "Đủ rồi. Đây chắc chắn là án mạng. Không phải tự sát."
    
    # Chuyển sang vòng lặp điều tra (để người chơi tự do đi lại và Kết Tội)
    jump m2_nav_loop

# Screen điều tra thi thể Arthur
screen m2_scr_phase4_investigation():
    # Background đã là map02_backyard (ảnh thi thể)
    
    # 1. Dây cước (Fishing Line) - Pick up items
    if not m2_clue_fishing_line:
        imagebutton:
            idle Transform("images/map02/object/fishing_line.png", zoom=0.15) # Cần file này
            hover Transform("images/map02/object/fishing_line.png", zoom=0.17)
            xpos 1280 ypos 500 # Dời lại gần thắt lưng Arthur (bên phải hơn)
            action [
                SetVariable("m2_clue_fishing_line", True),
                AddToSet(m2_inventory, "fishing_line"),
                Notify("Đã nhặt: Cuộn dây cước dính máu"),
                Function(m2_add_note, "Dây cước: Tìm thấy trong túi Arthur. Có vệt máu lạ ở giữa dây.")
            ]
            tooltip "Cuộn dây cước"

    # 2. Kiểm tra tay nạn nhân (Button to trigger dialogue)
    # Có thể là nút text hoặc click vào vùng tay
    textbutton "KIỂM TRA TAY NẠN NHÂN":
        text_size 30
        text_color "#fff"
        background Frame(Solid("#00000090"), 10, 10) # Nền đen nhạt bán trong suốt
        hover_background Frame(Solid("#000000b0"), 10, 10)
        align (0.5, 0.2)
        action Jump("m2_examine_hand")
        
    # Nút Quay lại NAV
    imagebutton:
        idle "images/ui/back_arrow.png" hover "images/ui/back_arrow.png" # Dùng icon quay lại
        align (0.05, 0.05)
        action Jump("m2_nav_loop")

# Label kiểm tra tay (để show hội thoại dài dòng)
label m2_examine_hand:
    m2_player "{i}Mu bàn tay phải sưng tấy. Có một lỗ thủng nhỏ, sâu, tụ máu tròn.{/i}"
    m2_player "{i}Bên trong vết thương dính... mực xanh? Đây không phải vết thương do ngã!{/i}"
    
    $ m2_clue_arthur_hand = True
    $ m2_add_note("Tay Arthur: Vết thủng tròn sâu, dính mực xanh.")
    
    call screen m2_scr_phase4_investigation

# Screen hiển thị thoại nhanh (Overlay)
screen m2_dialogue_overlay(txt):
    modal True
    frame:
        align (0.5, 0.8)
        padding (20, 20)
        background "#000c"
        text txt color "#fff" size 28 xsize 800 layout "subtitle"
    
    # Click để tắt
    button:
        action Hide("m2_dialogue_overlay")
