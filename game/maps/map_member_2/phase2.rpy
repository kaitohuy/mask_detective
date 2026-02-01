
label m2_phase2:
    # --- GIAI ĐOẠN 2: VỤ ÁN THỨ NHẤT (MURDER 1) ---
    
    # Âm thanh: Căng thẳng
    play music m2_bgm_tension fadein 1.0 loop
    
    # CẢNH 3: VỤ TRỘM BÍ ẨN (23:00 PM)
    scene black with fade
    "23:00 PM."
    play sound thunder
    "ĐÙNG ĐOÀNG! Tiếng sấm nổ rất lớn."
    "Tiếng bước chân chạy thình thịch."
    
    scene bg map02_hallway with fade
    
    show isabella normal at center with moveinright
    m2_isabella "Mọi người! Phòng Trưng Bày... có chuyện rồi!"
    
    scene bg map02_gallery_empty with fade
    
    m2_player "Trống trơn? Hàng trăm cái mặt nạ đã bốc hơi sao?"
    
    # CẢNH 4: CĂN PHÒNG ĐẪM MÁU
    
    # SFX: Tiếng đập cửa mạnh
    play sound "audio/fall.mp3"
    "RẦM!!!"
    "Một tiếng va đập cực lớn từ tầng trên."
    
    m2_player "Tiếng động từ phòng bà Rosalind! Mau lên!"
    
    # Hành lang
    scene bg map02_hallway with fade
    show sebastian normal at center
    m2_sebastian "Bà chủ! Bà chủ!"
    
    "Cửa khóa chặt. Không có tiếng trả lời."
    
    m2_player "Tránh ra! Phá cửa!"
    
    # SFX: Tiếng phá cửa/Gỗ gãy
    play sound "audio/break_door.mp3"
    "RẦM!"
    
    # Hiện trường
    scene bg map02_rosalind_bedroom_dead with fade
    
    "Hiện trường kinh hoàng: Bà Rosalind chết trên giường, một con dao găm cắm ngập ngực."
    "Sàn nhà ngập tràn mặt nạ, vây quanh giường như một nghi lễ quái dị."
    
    show isabella normal at right
    m2_isabella "Khủng khiếp quá... Mấy cái mặt nạ... chúng vây quanh bà ấy..."
    
    m2_player "{i}(Cửa sổ hàn kín. Cửa chính vừa bị phá chốt. Không có ai trong phòng ngoài nạn nhân.){/i}"
    
    "Mọi người lùi lại giữ nguyên hiện trường."
    
    return
