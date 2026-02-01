
# --------------------------------------------------------------------------------
# MAIN CONTROLLER (ĐIỀU PHỐI CÁC GIAI ĐOẠN)
# --------------------------------------------------------------------------------

label map2_start:
    
    # 1. Intro
    call m2_phase0
    
    # 2. Tiệc trà & Tham quan
    call m2_phase1
    
    # 3. Vụ án 1 (Rosalind)
    call m2_phase2
    
    # 4. Khoảng lặng / Điều tra tự do
    # Người chơi phải tự chạy qua lại các phòng để tìm manh mối
    call m2_phase3
    
    # 5. Vụ án 2 (Arthur)
    call m2_phase4
    
    # 6. Đối chất & Kết thúc (Được gọi qua Jump từ Phase 4/Accusation nên không cần Call nữa)
    # call m2_phase5
    
    return
