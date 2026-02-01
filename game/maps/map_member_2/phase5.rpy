
label m2_phase5:
    # --- GIAI ĐOẠN 5: ĐỐI CHẤT & VẠCH TRẦN ---
    
    # Âm thanh: Cao trào
    play music m2_bgm_climax fadein 1.0 loop
    
    # Bối cảnh tiếp nối từ Accusation (Sảnh chính)
    scene bg map02_livingroom 
    
    # Hiển thị lại nhân vật (vì vừa chuyển cảnh)
    show sebastian normal at left
    show liam normal at center
    show clara normal at right
    
    # Logic: Player đã nhập "Bút" -> Kết nối chứng cứ
    m2_player "Vật chứng đó chính là cây bút!"
    m2_player "Arthur bị sát hại. Tôi cần lập biên bản ngay. Mọi người cho tôi mượn bút được không? Bút của tôi hết mực rồi."
    
    # Kiểm tra bút
    m2_player "Bác sĩ Liam, ông luôn mang theo cây Parker mà? Cho tôi mượn chút."
    m2_liam "À... ừ... Cây đó tôi... vừa làm rơi hỏng rồi."
    
    m2_player "Không sao, đưa tôi xem thử."
    
    "Bác sĩ Liam miễn cưỡng đưa cây bút."
    
    # [Tương tác: Cây bút Parker]
    $ m2_clue_parker_pen = True
    m2_player "Nhìn xem. Ngòi bút kim loại cứng như vậy mà bị tòe đầu và cong gập 30 độ." 
    m2_player "Ở kẽ nắp bút còn dính vết nâu đỏ. Bác sĩ, ông nói 'làm rơi' sao?" 
    m2_player "Hay là ông đã dùng nó đâm mạnh vào tay Arthur khi cậu ta bám vào lan can?"
    
    m2_liam "Cậu... cậu vu khống!"
    
    m2_player "Vết thương trên tay Arthur là một lỗ thủng tròn dính mực xanh. Trùng khớp hoàn toàn với cây bút hỏng này."
    
    # Giải thích thủ thuật Con dao mặt nạ
    m2_player "Còn về bà Rosalind. Ông đã dùng thủ thuật 'Con dao mặt nạ'."
    m2_player "Đánh thuốc mê. Luồn dây qua ô thoáng. Xâu mặt nạ vào dây."
    m2_player "Khi kéo căng dây từ bên ngoài, hàng trăm chiếc mặt nạ ép chặt vào nhau, hóa thành một cây thương cứng."
    m2_player "Ông đâm bà ấy từ xa, qua khe cửa hẹp đó."
    
    m2_liam "Trí tưởng tượng phong phú đấy. Bằng chứng đâu?"
    
    # Bằng chứng thép
    m2_player "Thủ thuật này cần một lực kéo dây cực lớn. Sợi dây cước sẽ cắt vào da thịt người kéo."
    m2_player "Cuộn dây trong túi Arthur có một vệt máu lạ nằm ở giữa cuộn dây. Đó là máu của hung thủ."
    m2_player "Bác sĩ Liam, làm ơn tháo găng tay y tế bên tay phải ra."
    
    m2_liam "Không... Tay tôi bị dị ứng..."
    
    show sebastian normal at left
    m2_sebastian "Nếu ông trong sạch, xin hãy tháo ra."
    
    "Liam run rẩy tháo găng tay. Ngón trỏ tay phải quấn băng gạc đẫm máu."
    
    m2_player "Vết cứa sâu hoắm chạy ngang ngón tay. Dấu tích không thể chối cãi."
    
    # KẾT THÚC (TRUE ENDING)
    m2_liam "Ha ha ha..."
    "Liam gục xuống ghế, cười chua chát."
    
    m2_liam "Bà ta... mụ già đó... Bà ta ép tôi làm việc không công cả đời để trả nợ. Bà ta dồn tôi vào đường chết!"
    
    show isabella normal at right
    m2_isabella "Còn Arthur? Anh ấy vô tội mà!"
    
    m2_liam "Nó là vật thế thân hoàn hảo. Chỉ không ngờ nó bám dai như đỉa ở lan can... Tôi buộc phải dùng cây bút..."
    
    m2_player "Ông đã dùng những chiếc mặt nạ vô tri để giết người. Nhưng chính khuôn mặt thật của ông mới là thứ đáng sợ nhất."
    
    "Cảnh sát ập vào. Bão tan. Ánh sáng chiếu vào những chiếc mặt nạ rơi vãi trên sàn."
    
    # --- TRUE ENDING SEQUENCE ---
    scene bg m2_true_ending with fade
    
    # Text hiển thị kiểu Intro/Outro (tự động chạy)
    centered "{size=40}{font=fonts/kvn-97.ttf}Vụ án khép lại.{/font}{/size}" with Dissolve(2.0)
    centered "{size=35}{font=fonts/kvn-97.ttf}Những chiếc mặt nạ đã được gỡ xuống.\nSự thật trần trụi được phơi bày dưới ánh sáng công lý.{/font}{/size}" with Dissolve(3.0)
    centered "{size=35}{font=fonts/kvn-97.ttf}Nhưng liệu... lòng người có thực sự bình yên?{/font}{/size}" with Dissolve(3.0)
    
    "{b}TRUE ENDING - THÁM TỬ ĐẠI TÀI{/b}"
    return

# --- BAD ENDING (Dùng khi người chơi thất bại hoặc bỏ cuộc) ---
label m2_bad_ending:
    scene bg m2_bad_ending with fade
    
    centered "{size=40}{font=fonts/kvn-97.ttf}Vụ án đi vào ngõ cụt.{/font}{/size}" with Dissolve(2.0)
    centered "{size=35}{font=fonts/kvn-97.ttf}Hung thủ vẫn nhởn nhơ ngoài vòng pháp luật.\nBiệt thự Whitechapel chìm trong bóng tối vĩnh cửu.{/font}{/size}" with Dissolve(3.0)
    
    "{b}BAD ENDING - MÀN ĐÊM BUÔNG XUỐNG{/b}"
    return
