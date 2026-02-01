
# --------------------------------------------------------------------------------
# HỆ THỐNG KẾT TỘI & SUY LUẬN (ACCUSATION SYSTEM)
# --------------------------------------------------------------------------------

# Biến lưu trạng thái
default m2_suspect_chosen = ""
default m2_evidence_chosen = ""

# 1. BẮT ĐẦU KẾT TỘI
label m2_start_accusation:
    scene bg map02_livingroom with fade
    # stop music fadeout 2.0 # Cũ
    play music m2_bgm_climax fadein 1.0 loop # Mới: Nhạc phá án (nhac_pha_an.mp3)
    
    # Không show sprite ở đây nữa vì screen m2_suspect_selection đã hiển thị imagebutton rồi -> Tránh bị nhân đôi
    
    m2_player "Mọi người, tôi đã có đủ bằng chứng để vạch trần hung thủ."
    "Hãy chọn người mà bạn nghi ngờ nhất."
    
    call screen m2_suspect_selection
    
    # Sau khi chọn nghi phạm -> Chọn bằng chứng
    "Bạn muốn dùng bằng chứng nào để buộc tội [m2_suspect_chosen]?"
    
    call screen m2_evidence_selection
    
    # Xử lý Logic
    call m2_validate_accusation
    return

# 2. MÀN HÌNH CHỌN NGHI PHẠM
screen m2_suspect_selection():
    modal True
    
    # Sebastian
    imagebutton:
        focus_mask True
        idle Transform("sebastian normal", zoom=1.0)
        hover Transform("sebastian normal", zoom=1.0, matrixcolor=BrightnessMatrix(0.2))
        align (0.2, 0.85)
        action [SetVariable("m2_suspect_chosen", "Sebastian"), Return()]
        
    # Liam
    imagebutton:
        focus_mask True
        idle Transform("liam normal", zoom=1.0)
        hover Transform("liam normal", zoom=1.0, matrixcolor=BrightnessMatrix(0.2))
        align (0.5, 0.85)
        action [SetVariable("m2_suspect_chosen", "Liam"), Return()]

    # Clara
    imagebutton:
        focus_mask True
        idle Transform("clara normal", zoom=1.0)
        hover Transform("clara normal", zoom=1.0, matrixcolor=BrightnessMatrix(0.2))
        align (0.8, 0.85)
        action [SetVariable("m2_suspect_chosen", "Clara"), Return()]
        
    # Isabella (Họa sĩ - Người dùng yêu cầu thêm)
    imagebutton:
        focus_mask True
        # Isabella đứng hơi lệch một chút hoặc chen vào giữa
        idle Transform("isabella normal", zoom=0.9)
        hover Transform("isabella normal", zoom=0.9, matrixcolor=BrightnessMatrix(0.2))
        align (0.35, 0.85) # Đặt giữa Sebastian và Liam
        action [SetVariable("m2_suspect_chosen", "Isabella"), Return()]
        
    text "CHỌN HUNG THỦ" size 40 color "#fff" align (0.5, 0.1) outlines [(2, "#000", 0, 0)]

    # Nút Quay lại điều tra (Huỷ kết tội)
    textbutton "QUAY LẠI":
        text_font "fonts/kvn-97.ttf"
        text_size 25
        text_color "#fff"
        background Frame(Solid("#4E342E"), 10, 10) # Màu nâu đậm cho dễ đọc
        hover_background Frame(Solid("#5D4037"), 10, 10)
        padding (10, 5)
        align (0.82, 0.12) # Xếp ngay dưới nút Kết Tội (0.82, 0.05)
        action Jump("m2_nav_loop")

label m2_accuse_evidence_loop:
    # Sau khi chọn nghi phạm -> Chọn bằng chứng
    "Bạn muốn dùng bằng chứng nào để buộc tội [m2_suspect_chosen]?"
    
    call screen m2_evidence_selection
    
    # Logic xử lý từng bằng chứng (Loop)
    # Nếu chọn bằng chứng thường -> Show thoại -> Jump loop
    # Nếu chọn Kết Luận -> Jump Final Input
    
# 3. MÀN HÌNH CHỌN BẰNG CHỨNG (Lấy từ notebook)
screen m2_evidence_selection():
    modal True
    
    frame:
        background Frame("images/ui/ui_text.png", 50, 50)
        align (0.5, 0.5)
        padding (50, 50)
        xsize 800 ysize 600
        
        vbox:
            spacing 20
            text "CHỌN BẰNG CHỨNG" size 30 color "#f39c12" xalign 0.5 font "fonts/kvn-97.ttf"
            
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                ysize 350
                vbox:
                    spacing 10
                    for note in m2_notebook_list:
                        # Mỗi dòng note là một nút bấm
                        textbutton "[note]":
                            text_layout "subtitle" # Fix: text_style -> text_layout (subtitle is a layout mode)
                            text_size 22
                            text_color "#fff"
                            text_hover_color "#f1c40f"
                            action [SetVariable("m2_evidence_chosen", note), Hide("m2_evidence_selection"), Jump("m2_check_evidence_dialogue")] # Jump qua label check

            null height 20
            
            # Nút KẾT LUẬN (Khi đã hết bằng chứng)
            textbutton "ĐƯA RA VẬT CHỨNG QUYẾT ĐỊNH":
                text_size 30
                text_color "#e74c3c"
                background Frame(Solid("#fff"), 5, 5)
                xalign 0.5
                action [Hide("m2_evidence_selection"), Jump("m2_final_deduction_input")]

# Xử lý hội thoại cho từng bằng chứng (tạm thời gộp chung logic cũ)
label m2_check_evidence_dialogue:
    # HIỂN THỊ LẠI CÁC NHÂN VẬT (Vì từ screen jump qua sẽ mất layer)
    scene bg map02_livingroom # Đảm bảo nền
    show sebastian normal at left
    show liam normal at center
    show clara normal at right
    # show isabella normal at right # (Tùy chọn nếu cần)

    if m2_suspect_chosen == "Liam":
        if "Victor" in m2_evidence_chosen or "mặt nạ" in m2_evidence_chosen or "dây" in m2_evidence_chosen:
            m2_player "Bác sĩ Liam, những vết xước trên mặt nạ và ô thoáng cửa sổ..."
            m2_player "Chứng tỏ hung thủ đã dùng thủ thuật kéo dây từ bên ngoài. Và nãy tôi thấy ngón tay ông bị thương."
            m2_liam "Tay tôi bị... dao gọt hoa quả cắt trúng thôi."
        elif "trà" in m2_evidence_chosen:
            m2_player "Trong tách trà của bà Rosalind có thuốc mê. Ông là bác sĩ, ông là người dễ dàng có được loại thuốc này nhất."
            m2_liam "Tôi kê đơn cho bà ấy mỗi ngày. Đó là thuốc an thần, không phải thuốc độc."
        else:
            m2_player "Bằng chứng này có vẻ chưa đủ sức nặng với hắn."
    else:
        m2_player "Người này có vẻ không liên quan tới chứng cứ này..."
        
    jump m2_accuse_evidence_loop # Quay lại chọn tiếp

# 4. XỬ LÝ KẾT QUẢ (Giữ nguyên logic Bút)
label m2_final_deduction_input:
    
    m2_player "Tuy nhiên, bằng chứng quan trọng nhất vẫn còn thiếu."
    m2_player "Vật chứng này kết nối trực tiếp hung thủ với cái chết của Arthur."
    
    # Input
    $ m2_final_answer = renpy.input("Nhập tên vật chứng quan trọng nhất:", length=20).strip().lower()
    
    if "bút" in m2_final_answer or "pen" in m2_final_answer:
        m2_player "Chính xác. Đó là cây bút!"
        jump m2_phase5 # Chuyển sang True Ending
    else:
        m2_player "Không.. đó không phải là thứ tôi đang nghĩ đến."
        "Gợi ý: Một vật dụng cá nhân của Liam, đã bị hỏng."
        jump m2_final_deduction_input
