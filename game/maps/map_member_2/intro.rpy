
label m2_phase0:
    # --- GIAI ĐOẠN 0: MÀN ĐÊM & SỰ BIẾN MẤT (INTRO) ---
    
    # 1. Âm thanh Intro: Bão
    play music m2_bgm_intro fadein 2.0 loop volume 0.8
    
    scene black
    show text "{size=50}{color=#e74c3c}Vụ Án 02: Huyết Nguyệt & Lời Nguyền Mặt Nạ{/color}{/size}" with dissolve
    pause 3.0
    hide text with dissolve

    scene bg map02_outside at slow_zoom_in with fade
    
    "Biệt thự Huyết Nguyệt (Blood Moon Manor) nằm trơ trọi trên vách đá sát biển."
    "Bão lớn đang đổ bộ. Tiếng sóng biển gầm gào hòa lẫn với tiếng sấm rền vang..."
    
    # Chuyển cảnh sang Phase 1
    return
