
label m2_phase1:
    # --- GIAI ĐOẠN 1: TIỆC TRÀ & THAM QUAN ---
    
    # 1. Âm thanh: Nhạc nhẹ/Hơi trầm (Piano)
    # Lưu ý: Nếu chưa có file nhạc thì Ren'Py sẽ báo lỗi file missing, cần đảm bảo file tồn tại hoặc comment lại.
    play music m2_bgm_calm fadein 2.0 loop
    
    # CẢNH 1: TIỆC TRÀ TRONG BÃO (19:00 PM)
    scene bg map02_livingroom with fade
    
    show rosalind normal at center
    m2_rosalind "Sebastian! Đóng rèm lại. Tiếng sóng biển hôm nay nghe như tiếng gào thét vậy. Ta đau đầu quá."
    
    show sebastian normal at left
    m2_sebastian "Thưa bà, cửa sổ đã được chốt kỹ. Tôi sẽ kéo thêm rèm nhung để giảm bớt tiếng ồn."
    
    hide sebastian
    show liam normal at right with moveinright
    m2_liam "Huyết áp của bà đang tăng đấy, Rosalind. Uống tách trà hoa cúc này đi. Tôi đã pha chế theo công thức riêng để giúp bà an thần."
    
    "Bác sĩ Liam rút từ túi áo ngực ra một cây bút Parker vỏ bạc sáng bóng, gõ nhẹ vào sổ tay y tế."
    m2_liam "Tôi đã ghi chú lại liều lượng. Bà nhớ uống hết khi còn ấm."
    
    m2_player "{i}(Cây bút Parker mạ bạc, ngòi bút còn mới tinh. Bác sĩ Liam quả là người kỹ tính.){/i}"
    
    m2_rosalind "Cảm ơn Liam. Trong cái nhà này, chắc chỉ còn ông là mong ta sống thọ... À, thằng Arthur đâu rồi?"
    
    hide liam
    show arthur nervous at left with moveinleft
    m2_arthur "Cháu... cháu đây thưa dì."
    
    m2_rosalind "Đừng có lấm lét như kẻ trộm thế. Trước khi ta đi nghỉ, ta muốn kiểm tra bộ sưu tập. Tất cả đi theo ta."

    # CẢNH 2: NHỮNG LINH HỒN GỐM SỨ (19:30 PM - PHÒNG TRƯNG BÀY)
    scene black with fade
    "Phòng Trưng Bày mặt nạ."
    
    # SFX: Tiếng bấm mật mã điện tử
    play sound "audio/ping.mp3"
    "Beep-Beep-Beep-Beep."
    
    # Dùng tạm background gallery empty hoặc background gallery có mặt nạ nếu có
    # Ở đây dùng gallery_empty tượng trưng hoặc tốt nhất là nên có background full
    scene bg map02_gallery_empty with fade 
    
    show rosalind normal at center
    m2_rosalind "Mở ra."
    
    # SFX: Tiếng cửa tự động mở
    play sound "audio/door_open.mp3"
    "Cánh cửa bật mở. Bên trong là 200 chiếc mặt nạ trắng toát dưới ánh đèn vàng."
    
    m2_rosalind "Nhìn kỹ đi. Đây là tài sản quý giá nhất của dòng họ."
    m2_rosalind "Khóa điện tử này được cài đặt theo ngày sinh của ta. Chỉ có ta, Liam và mi - Arthur, là biết mật mã."
    
    show arthur nervous at left
    m2_arthur "Vâng... vâng thưa dì. Cháu nhớ rồi."
    
    hide arthur
    show liam normal at right
    
    "Bà Rosalind cầm một chiếc mặt nạ lên, gõ vào nó."
    
    # SFX: Tiếng gõ vào gốm sứ (Keng Keng)
    play sound "audio/claze_hit.mp3"
    "Keng! Keng!"
    
    m2_rosalind "Nghe thấy không? Gốm nung nhiệt độ cao. Chúng cứng như đá và bề mặt láng mịn vĩnh cửu."
    m2_rosalind "Nếu mất dù chỉ một cái, ta sẽ tống cổ mi ra đường đấy Arthur."
    
    m2_liam "Bà Rosalind, thuốc bắt đầu ngấm rồi đấy. Bà nên về phòng nghỉ."
    
    m2_rosalind "Được rồi... Tất cả ra ngoài đi. Ta sẽ về phòng và chốt cửa (Deadbolt) ngay lập tức. Đêm nay ta có linh cảm không lành."

    return
